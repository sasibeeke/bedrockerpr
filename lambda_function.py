import json
import boto3
import urllib.request
import os

def lambda_handler(event, context):
    print("ENV:", os.environ)
    print("TOKEN:", os.environ.get('GITHUB_TOKEN'))

    body = json.loads(event.get('body', '{}'))

    # Only trigger on PR open or new commit
    if body.get('action') not in ['opened', 'synchronize']:
        return {'statusCode': 200, 'body': 'Ignored'}

    pr_number = body['pull_request']['number']
    repo_full_name = body['repository']['full_name']
    diff_url = body['pull_request']['diff_url']
    github_token = os.environ['GITHUB_TOKEN']

    # Fetch PR diff
    req = urllib.request.Request(
        diff_url,
        headers={'Authorization': f'token {github_token}'}
    )
    with urllib.request.urlopen(req) as response:
        diff = response.read().decode('utf-8')[:8000]

    # Bedrock client
    bedrock = boto3.client('bedrock-runtime', region_name='us-east-1')

    prompt = f"""You are a senior code reviewer. Review this PR diff and give:
1. Summary of changes
2. Bugs or issues found
3. Security concerns
4. Suggestions for improvement

PR Diff:
{diff}

Keep feedback concise and actionable."""

    # ✅ NOVA MODEL (UPDATED)
    response = bedrock.invoke_model(
        modelId='amazon.nova-lite-v1:0',
        body=json.dumps({
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {"text": prompt}
                    ]
                }
            ],
            "inferenceConfig": {
                "maxTokens": 1000,
                "temperature": 0.5
            }
        })
    )

    # ✅ NOVA RESPONSE PARSING
    result = json.loads(response['body'].read())
    review = result['output']['message']['content'][0]['text']

    # Post comment to GitHub PR
    comment_url = f"https://api.github.com/repos/{repo_full_name}/issues/{pr_number}/comments"

    comment_data = json.dumps({
        "body": f"## 🤖 AI Code Review\n\n{review}"
    }).encode('utf-8')

    req = urllib.request.Request(
        comment_url,
        data=comment_data,
        headers={
            'Authorization': f'token {github_token}',
            'Content-Type': 'application/json'
        },
        method='POST'
    )

    urllib.request.urlopen(req)

    return {'statusCode': 200, 'body': 'Review posted!'}
