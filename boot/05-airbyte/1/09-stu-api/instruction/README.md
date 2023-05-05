# Instruction 

## Task 

Extract data from github

**Generate github access token**

1. Go to GitHub and select "Settings" 
2. Go to "Developer settings" 
3. Go to "Personal access tokens" 
4. Select "Generate new token" 
5. Tick scope "repo" and provide a note
6. Select "Generate" 
7. Make sure to save the token someplace secure

**Create new airbyte source**

1. Go to sources
2. Select "GitHub" 
3. Authentication: "OAuth" > paste your access token 
4. Start date: `2020-01-01T00:00:00Z` 
5. GitHub repositories: `Data-Engineer-Camp/sample-repo-airbyte` 
6. Select "Set up source" 

**Create new airbyte connection**

1. Go to connection 
2. Sync only `commits` 
