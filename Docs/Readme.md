# User Stories

1. As a person in the local community I want to be able to bring attention to issues within my community so they can be resovled.
2. As a person in the local community I want to be able to see what issues are present in my community so I can help fix them.
3. As a local leader I want to be able to see what issues are important to the local community so I can help resovle them. 
4. As a future local leader I want to see what issues are important to the voters so I can know where to direct my campaign.

## Acceptance Criteria

1. In order to fulfil user story 1 the users must be able to POST issues to the Community Process app.
2. In order to fulfil user story 2 users must be able to GET a list of issues from the Community Process app.
3. To fulful user story 3 users must be able to respond to POSTed issues and it must be clear when a local leader has agreed with an issue.
4. To fulfil user story 4 users must be able to agree with issues and the list needs to be sortable by most to least agreed on issues.

# Mis User Stories

1. As a local user I want to boost my issues to the top of the list by voting repeatedly on my POSTed issues multiple times.
2. As a non-local user I want to upset the local users by making fake issues.
3. As a hacker I want to gather the personal data of other users by exploting a vulnerability to gain access to the back-end database.

# Mitigations

1. To mitigate the mis user story 1 users who have voted should be remembered so they can only vote once on each issue.
2. To mitigate the mis user story 2 the application process should require some form of local identification to prevent non-locals from being able to POST or vote on issues.
3. To mitigate the mis user story 3 guidelines to prevent exploiting should be followed and the database should be encrypted in case of unknown vulnerabilities. 