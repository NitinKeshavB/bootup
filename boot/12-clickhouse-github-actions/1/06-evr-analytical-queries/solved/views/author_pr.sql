CREATE VIEW IF NOT EXISTS author_pr 
as 
SELECT
    actor_login,
    uniq(repo_name, number) AS prs
FROM github
WHERE (event_type = 'PullRequestReviewCommentEvent') AND (action = 'created')
GROUP BY actor_login
ORDER BY uniq(repo_name, number) desc
