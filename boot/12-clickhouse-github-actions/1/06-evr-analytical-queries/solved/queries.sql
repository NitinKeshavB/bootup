-- taken from: https://ghe.clickhouse.tech/

-- All records 
select * from github; 

-- Total stars 
select count() from github where event_type = 'WatchEvent'

-- Stars over the years
select
    year,
    lower(repo_name) as repo,
    count()
from github
where (event_type = 'WatchEvent') and (year >= 2015)
group by
    repo,
    toYear(created_at) as year
order by
    year asc,
    count() desc


-- Total number of contributors 
select uniq(actor_login) from github


-- The most tough code reviews
select
    concat('https://github.com/', repo_name, '/pull/', toString(number)) as url,
    uniq(actor_login) as authors
from github
where (event_type = 'PullRequestReviewCommentEvent') and (action = 'created')
group by
    repo_name,
    number
order by authors desc

-- Authors with the most pushes
select
    actor_login,
    count() as c,
    uniq(repo_name) AS repos
from github
where event_type = 'PushEvent'
group by actor_login
order by c desc

-- Total number of issues
SELECT count() FROM github WHERE event_type = 'IssueCommentEvent'

-- The proportion between issue comments and issues
SELECT
    repo_name,
    count() AS comments,
    uniq(number) AS issues,
    round(comments / issues, 2) AS ratio
FROM github
WHERE event_type = 'IssueCommentEvent'
GROUP BY repo_name
ORDER BY count() DESC

-- Authors with most number of PRs 
SELECT
    actor_login,
    uniq(repo_name, number) AS prs
FROM github
WHERE (event_type = 'PullRequestReviewCommentEvent') AND (action = 'created')
GROUP BY actor_login
ORDER BY uniq(repo_name, number) DESC

-- Top labels for issues and pull requests 
SELECT
    arrayJoin(labels) AS label,
    count() AS c
FROM github
WHERE (event_type IN ('IssuesEvent', 'PullRequestEvent', 'IssueCommentEvent')) AND (action IN ('created', 'opened', 'labeled'))
GROUP BY label
ORDER BY c DESC
