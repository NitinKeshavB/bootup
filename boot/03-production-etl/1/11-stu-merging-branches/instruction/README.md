# Instruction 

## Task 

1. Checkout to the main branch 

    run: 
    ```
    git checkout main 
    ```

2. Check the log 

    run: 
    ```
    git log
    ```

    output: 
    ```
    commit 03acfb953fad9635078b72f062f573cdf37ab5a1 (HEAD -> main, origin/main, my-new-branch-1)
    Author: Jonathan Neo <jonathanneo@me.com>
    Date:   Wed Aug 3 22:58:05 2022 +0800

        Create hello_person.py

    commit 005a59d36b9bffc5eb96cad6f2098fc6c7797232
    Author: Jonathan Neo <jonathanneo@me.com>
    Date:   Wed Aug 3 22:40:56 2022 +0800

        added bye world

    commit 1f8c2f525002c3729e1e5b21553bbc77e5672778
    Author: Jonathan Neo <jonathanneo@me.com>
    Date:   Wed Aug 3 22:29:22 2022 +0800

        hello world
    ```

    Note: It does not have the new changes from `my-new-branch-2`. 


3. Merge the feature branch to the main branch 

    run: 
    ```
    git merge my-new-branch-2
    ```

    output: 
    ```
    Updating 03acfb9..86e4fbd
    Fast-forward
    color_world.py | 2 ++
    hello_world.py | 2 +-
    2 files changed, 3 insertions(+), 1 deletion(-)
    create mode 100644 color_world.py
    ```

    Note: the `main` branch has now been updated with `my-new-branch-2` changes. 

4. Check the log 

    run: 
    ```
    git log
    ```

    output: 
    ```
    commit 86e4fbdabb8775353db2c5aa0b3714fd554b962e (HEAD -> main, origin/my-new-branch-2, my-new-branch-2)
    Author: Jonathan Neo <jonathanneo@me.com>
    Date:   Wed Aug 3 23:22:42 2022 +0800

        color world

    commit 03acfb953fad9635078b72f062f573cdf37ab5a1 (origin/main, my-new-branch-1)
    Author: Jonathan Neo <jonathanneo@me.com>
    Date:   Wed Aug 3 22:58:05 2022 +0800

        Create hello_person.py

    commit 005a59d36b9bffc5eb96cad6f2098fc6c7797232
    Author: Jonathan Neo <jonathanneo@me.com>
    Date:   Wed Aug 3 22:40:56 2022 +0800

        added bye world

    commit 1f8c2f525002c3729e1e5b21553bbc77e5672778
    Author: Jonathan Neo <jonathanneo@me.com>
    Date:   Wed Aug 3 22:29:22 2022 +0800

        hello world
    ```

5. Git push 

    run: 
    ```
    git push 
    ```

    Note: We have now updated the remote `origin/main` with the changes. 

