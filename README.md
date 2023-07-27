# README
- 강의장에서 공부한 내용
- 현재 레포지터리 리모트 닉네임 = TIL




### git 설정 초기화
```bash
# vim을 활용해서 설정 제거하기
# vim git 설정 파일 열기
$ vim ~/.gitconfig
# inser 키 : 수정 상태 만들기
# --insert-- 인 상태에서 모든 내용 삭제
# esc: 수정 상태 종료
# :wq
```

- code ~/.gitconfig : vscode에서 수정하기


### Cycle

1. 폴더 만들기
2. touch README.md   로 파일 만들 수도 있음
3. git add README.md
4. git commit -m " 이름적고 "

5. 새 레포지터리 만들어서 이름 정하고 : 이건 깃허브에서

6. git init 후 -> 
    git remote add origin {복사한 레포지터리경로}
7. git push origin master 로 깃에 올리기
8. 잘올라갔는지 확인하기

### 하나 더 만드려면?
git remote add origin 하면 이미 있는 이름
git remote add second로 새로운 이름 만들기
git push second master
레포지터리 여러개 만들어서 여러군데 올릴 수 있는 것!

원격저장소에 있는 애랑 로컬에서 작업하고 있는 애랑 같은 깃폴더에 있는걸로 관리

★★★ git push origin(리모트 닉네임) master 하면 나의 github에 올라간다!! ★★★

### 원격 저장소에 업로드
```bash
$ git remote add{remote_nickname}{remote_url}
# git remote add origin {내 깃허브 주소}
```
git remote remove origin -> 주소 잘못 설정했을 때 지우는 것