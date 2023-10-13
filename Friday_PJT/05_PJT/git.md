SSAFY@DESKTOP-MDJG1NJ MINGW64 ~/Desktop/Practice
$ git init
Initialized empty Git repository in C:/Users/SSAFY/Desktop/Practice/.git/

SSAFY@DESKTOP-MDJG1NJ MINGW64 ~/Desktop/Practice (master)
$ git branch login
fatal: not a valid object name: 'master'

SSAFY@DESKTOP-MDJG1NJ MINGW64 ~/Desktop/Practice (master)
$ touch text.txt

SSAFY@DESKTOP-MDJG1NJ MINGW64 ~/Desktop/Practice (master)
$ git add .

SSAFY@DESKTOP-MDJG1NJ MINGW64 ~/Desktop/Practice (master)
$ git commit -m "첫번째작업물"
[master (root-commit) cf3eace] 첫번째작업물
 1 file changed, 1 insertion(+)
 create mode 100644 text.txt

SSAFY@DESKTOP-MDJG1NJ MINGW64 ~/Desktop/Practice (master)
$ git log
commit cf3eace9c2c00e4aba87af7c4d82f4250adeb1ca (HEAD -> master)
Author: Jo-hye-won <a01051910573@gmail.com>
Date:   Fri Oct 13 11:45:47 2023 +0900

    첫번째작업물

SSAFY@DESKTOP-MDJG1NJ MINGW64 ~/Desktop/Practice (master)
$ git branch login

SSAFY@DESKTOP-MDJG1NJ MINGW64 ~/Desktop/Practice (master)
$ git branch
  login
* master

SSAFY@DESKTOP-MDJG1NJ MINGW64 ~/Desktop/Practice (master)
$ git switch login
Switched to branch 'login'

SSAFY@DESKTOP-MDJG1NJ MINGW64 ~/Desktop/Practice (login)
$ touch login.txt

SSAFY@DESKTOP-MDJG1NJ MINGW64 ~/Desktop/Practice (login)
$ git add .

SSAFY@DESKTOP-MDJG1NJ MINGW64 ~/Desktop/Practice (login)
$ git commit -m "로그인 작업"
[login 36422fe] 로그인 작업
 1 file changed, 1 insertion(+)
 create mode 100644 login.txt

SSAFY@DESKTOP-MDJG1NJ MINGW64 ~/Desktop/Practice (login)
$ git switch master
Switched to branch 'master'

SSAFY@DESKTOP-MDJG1NJ MINGW64 ~/Desktop/Practice (master)
$ git log
commit cf3eace9c2c00e4aba87af7c4d82f4250adeb1ca (HEAD -> master)
Author: Jo-hye-won <a01051910573@gmail.com>
Date:   Fri Oct 13 11:45:47 2023 +0900

    첫번째작업물

SSAFY@DESKTOP-MDJG1NJ MINGW64 ~/Desktop/Practice (master)
$ git switch login
Switched to branch 'login'

SSAFY@DESKTOP-MDJG1NJ MINGW64 ~/Desktop/Practice (login)
$ got switch master
bash: got: command not found

SSAFY@DESKTOP-MDJG1NJ MINGW64 ~/Desktop/Practice (login)
$ git log
commit 36422fed466e9d0917fb24a3a05ef37a18d0f242 (HEAD -> login)
Author: Jo-hye-won <a01051910573@gmail.com>
Date:   Fri Oct 13 11:48:46 2023 +0900

    로그인 작업

commit cf3eace9c2c00e4aba87af7c4d82f4250adeb1ca (master)
Author: Jo-hye-won <a01051910573@gmail.com>
Date:   Fri Oct 13 11:45:47 2023 +0900

    첫번째작업물

SSAFY@DESKTOP-MDJG1NJ MINGW64 ~/Desktop/Practice (login)
$ git switch login
Already on 'login'

SSAFY@DESKTOP-MDJG1NJ MINGW64 ~/Desktop/Practice (login)
$ git log --oneline
36422fe (HEAD -> login) 로그인 작업
cf3eace (master) 첫번째작업물

SSAFY@DESKTOP-MDJG1NJ MINGW64 ~/Desktop/Practice (login)
$ git switch master
Switched to branch 'master'

SSAFY@DESKTOP-MDJG1NJ MINGW64 ~/Desktop/Practice (master)
$ git branch article

SSAFY@DESKTOP-MDJG1NJ MINGW64 ~/Desktop/Practice (master)
$ git switch article
Switched to branch 'article'

SSAFY@DESKTOP-MDJG1NJ MINGW64 ~/Desktop/Practice (article)
$ touch article.txt

SSAFY@DESKTOP-MDJG1NJ MINGW64 ~/Desktop/Practice (article)
$ git add .

SSAFY@DESKTOP-MDJG1NJ MINGW64 ~/Desktop/Practice (article)
$ git commit -m"게시글 작업"
[article 3d2b2a8] 게시글 작업
 1 file changed, 1 insertion(+)
 create mode 100644 article.txt

SSAFY@DESKTOP-MDJG1NJ MINGW64 ~/Desktop/Practice (article)
$ git log --oneline
3d2b2a8 (HEAD -> article) 게시글 작업
cf3eace (master) 첫번째작업물

SSAFY@DESKTOP-MDJG1NJ MINGW64 ~/Desktop/Practice (article)
$ git add .

SSAFY@DESKTOP-MDJG1NJ MINGW64 ~/Desktop/Practice (article)
$ git commit -m"게시글 수정"
[article 8be9ee0] 게시글 수정
 1 file changed, 2 insertions(+), 1 deletion(-)

SSAFY@DESKTOP-MDJG1NJ MINGW64 ~/Desktop/Practice (article)
$ git log --oneline
8be9ee0 (HEAD -> article) 게시글 수정
3d2b2a8 게시글 작업
cf3eace (master) 첫번째작업물

SSAFY@DESKTOP-MDJG1NJ MINGW64 ~/Desktop/Practice (article)
$ git switch master
Switched to branch 'master'

SSAFY@DESKTOP-MDJG1NJ MINGW64 ~/Desktop/Practice (master)
$ git merge login
Updating cf3eace..36422fe
Fast-forward
 login.txt | 1 +
 1 file changed, 1 insertion(+)
 create mode 100644 login.txt

SSAFY@DESKTOP-MDJG1NJ MINGW64 ~/Desktop/Practice (master)
$ git log --oneline
36422fe (HEAD -> master, login) 로그인 작업
cf3eace 첫번째작업물

SSAFY@DESKTOP-MDJG1NJ MINGW64 ~/Desktop/Practice (master)
$ git merge article
Merge made by the 'ort' strategy.
 article.txt | 2 ++
 1 file changed, 2 insertions(+)
 create mode 100644 article.txt

SSAFY@DESKTOP-MDJG1NJ MINGW64 ~/Desktop/Practice (master)
$ git log --oneline
c2f8f63 (HEAD -> master) Merge branch 'article'
8be9ee0 (article) 게시글 수정
3d2b2a8 게시글 작업
36422fe (login) 로그인 작업
cf3eace 첫번째작업물

SSAFY@DESKTOP-MDJG1NJ MINGW64 ~/Desktop/Practice (master)
$ git log --oneline --graph
*   c2f8f63 (HEAD -> master) Merge branch 'article'
|\
| * 8be9ee0 (article) 게시글 수정
| * 3d2b2a8 게시글 작업
* | 36422fe (login) 로그인 작업
|/
* cf3eace 첫번째작업물

SSAFY@DESKTOP-MDJG1NJ MINGW64 ~/Desktop/Practice (master)
$ git branch -d login
Deleted branch login (was 36422fe).

SSAFY@DESKTOP-MDJG1NJ MINGW64 ~/Desktop/Practice (master)
$ git branch -d article
Deleted branch article (was 8be9ee0).

SSAFY@DESKTOP-MDJG1NJ MINGW64 ~/Desktop/Practice (master)
$ git branch
* master

SSAFY@DESKTOP-MDJG1NJ MINGW64 ~/Desktop/Practice (master)
$ git switch -c logout
Switched to a new branch 'logout'

SSAFY@DESKTOP-MDJG1NJ MINGW64 ~/Desktop/Practice (logout)
$ git add .

SSAFY@DESKTOP-MDJG1NJ MINGW64 ~/Desktop/Practice (logout)
$ git commit -m"로그아웃 작업"
[logout bb53678] 로그아웃 작업
 1 file changed, 1 insertion(+)

SSAFY@DESKTOP-MDJG1NJ MINGW64 ~/Desktop/Practice (logout)
$ git switch master
Switched to branch 'master'

SSAFY@DESKTOP-MDJG1NJ MINGW64 ~/Desktop/Practice (master)
$ git add .

SSAFY@DESKTOP-MDJG1NJ MINGW64 ~/Desktop/Practice (master)
$ git commit -m"마스터가 작업"
[master 15d2513] 마스터가 작업
 1 file changed, 1 insertion(+)

SSAFY@DESKTOP-MDJG1NJ MINGW64 ~/Desktop/Practice (master)
$ git merge logout
Auto-merging text.txt
CONFLICT (content): Merge conflict in text.txt
Automatic merge failed; fix conflicts and then commit the result.

SSAFY@DESKTOP-MDJG1NJ MINGW64 ~/Desktop/Practice (master|MERGING)
$ git add .

SSAFY@DESKTOP-MDJG1NJ MINGW64 ~/Desktop/Practice (master|MERGING)
$ git commit -m "수정"
[master 3b05467] 수정

SSAFY@DESKTOP-MDJG1NJ MINGW64 ~/Desktop/Practice (master)
$ git status
On branch master
nothing to commit, working tree clean

SSAFY@DESKTOP-MDJG1NJ MINGW64 ~/Desktop/Practice (master)
$ git add .

SSAFY@DESKTOP-MDJG1NJ MINGW64 ~/Desktop/Practice (master)
$ git commit -m"컨플릭트 해결"
On branch master
nothing to commit, working tree clean

SSAFY@DESKTOP-MDJG1NJ MINGW64 ~/Desktop/Practice (master)
$ git log --oneline --gragh
fatal: unrecognized argument: --gragh

SSAFY@DESKTOP-MDJG1NJ MINGW64 ~/Desktop/Practice (master)
$ git log --oneline --graph
*   3b05467 (HEAD -> master) 수정
|\
| * bb53678 (logout) 로그아웃 작업
* | 15d2513 마스터가 작업
|/
*   c2f8f63 Merge branch 'article'
|\
| * 8be9ee0 게시글 수정
| * 3d2b2a8 게시글 작업
* | 36422fe 로그인 작업
|/
* cf3eace 첫번째작업물

SSAFY@DESKTOP-MDJG1NJ MINGW64 ~/Desktop/Practice (master)
$ ^C

SSAFY@DESKTOP-MDJG1NJ MINGW64 ~/Desktop/Practice (master)
$ git switch -c hyewon
Switched to a new branch 'hyewon'

SSAFY@DESKTOP-MDJG1NJ MINGW64 ~/Desktop/Practice (hyewon)
$ touch my_work.txt

SSAFY@DESKTOP-MDJG1NJ MINGW64 ~/Desktop/Practice (hyewon)
$ git add .

SSAFY@DESKTOP-MDJG1NJ MINGW64 ~/Desktop/Practice (hyewon)
$ git commit -m"내 작업물"
[hyewon 6e51146] 내 작업물
 1 file changed, 1 insertion(+)
 create mode 100644 my_work.txt

SSAFY@DESKTOP-MDJG1NJ MINGW64 ~/Desktop/Practice (hyewon)
$ git switch master
Switched to branch 'master'

SSAFY@DESKTOP-MDJG1NJ MINGW64 ~/Desktop/Practice (master)
$ git merge my_work
merge: my_work - not something we can merge

SSAFY@DESKTOP-MDJG1NJ MINGW64 ~/Desktop/Practice (master)
$ git merge hyewon
Updating 3b05467..6e51146
Fast-forward
 my_work.txt | 1 +
 1 file changed, 1 insertion(+)
 create mode 100644 my_work.txt
