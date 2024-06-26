# OSS Personal Project Phase1 : Wordle
# 구현 목표
#### 프로젝트의 목표는 유명한 게임인 Wordle을 Pygame으로 구현하는 것이다. 
#### Wordle은 숫자 야구처럼 시작 시 무작위하게 정답 단어가 결정이 되고, 플레이어는 해당 단어를 추측하는 게임이다. 숫자 야구와 비슷하게, 각 추측마다 색깔을 통해 정보를 제공한다. 각 추측에 있는 Letter마다 정답 단어에 존재하지 않으면 회색, 존재하지만 위치(Index)가 다르면 노란색, 존재하는 위치까지 같으면 초록색으로 나타내어준다. 
#### 총 6번의 추측기회가 주어지며 6회 이내에 맞추면 승리, 6회 이내에 맞추지 못하면 패배이다.

# 구현 기능
- pygame 기반 Game Screen 구현
- 키보드 입력을 통한 단어 추측
- 단어 추측시 색깔을 통해 정보 제공
- HINT 기능을 만들어 HINT 칸을 누르면 무작위하게 한 글자의 정보 제공
- Daily Mode와 Inf Mode를 제공
- Daily Mode의 경우 하루에 단 하나의 Word로만 Play가능, 게임이 끝나고 Enter 입력 시  Mode 선택 창으로 되돌아감
- Inf Mode의 경우 완전 Randomly하게 생성되는 Word로 연습가능한 Mode, 게임이 끝고 Enter 입력 시 새 게임 시작
# Reference
[1] <https://github.com/pygame/pygame> "pygame"

[2] <https://github.com/baraltech/Wordle-PyGame> "Wordle-pygame"
# 지원 OS 및 실행 방법
## 지원 OS
|OS| 지원 여부          |
|-----|-----------------|
|Windows| :o:           |
| Linux | :o:           |
| MacOS | :x:(확인필요) |
## 실행 방법
### Windows
1. python3.12를 설치한다.
2. Microsoft Visual c++ Build Tools 설치
```
1. https://visualstudio.microsoft.com/ko/visual-cpp-build-tools/ 에서   Build Tools 다운로드 후 실행

2. Visual Studio Installer가 실행 된 경우 해당 버전의 "수정(Modify)" 클릭

3. Desktop & Mobile 에서 c++ build Tools 체크 표시 이후 설치

4. 시스템 재부팅
```
3. powershell 창에서 pygame을 설치
```
pip install pygame
```
4. 재부팅 이후 python wordle.py 실행하면 게임 창이 뜨면서 게임을 할 수 있다.
### Linux
1. python3 설치
```
1. sudo apt-get install python3
```
2. pygame 설치
```
1. pip install pygame
```
3. 리포지토리 내부에서 wordle.py 실행
```
python3 wordle.py
```
# 실행 예시
![Wordle-_Ubuntu_-2024-06-05-21-39-36](https://github.com/RyuRaseul/OSS_Personal_Project_Phase1/assets/113527604/a2ab2988-1ca0-4846-810a-83b277a5ad4d)
# 코드 설명

## wordle.py
### class Tile
 i. def __init__ : 화면 상단부의 Word Tile 객체를 생성하는 함수

 ii. def draw : Word Tile을 screen에 나타내주는 함수
### class Letter
 i. def __init__ : 사용자가 입력한 Text 객체를 생성하는 함수

 ii. def draw : Letter 객체를 screen에 나타내주는 함수

 iii. def delete : Letter 객체를 덮어씌워 screen에서 없애주는 함수
### class Keyboard
 i. def __init__ : 화면 아래의 Keyboard 부분의 각 Key를 생성하는 함수

 ii. def draw : Keyboard 객체를 그려주는 함수
### def create\_letter()
 Player가 입력한 값을, 몇 번째 Letter인지, 몇 번쨰 추측인지를 고려하여 화면에 나타내주는 함수
### def delete\_letter()
 Player가 Backspace를 누르면 해당 Letter를 지워주는 함수
### def guess\_check(guessed\_word)
 Player가 입력한 5글자 Word(guessed\_word)를 확인하고 Word Tile 및 Keyboard에 회색, 노란색, 초록색으로 표시해주는 함수

 또한, Player의 추측이 맞았을 경우 게임을 끝낼 수 있도록 result 값을 결정해준다.
### def make\_tiles()
 게임 시작시 모든 Word Tile을 생성하고 그려주는 함수
### def Mode\_Select()
 Mode 선택 창을 생성하는 함수
### def game\_end()
 Player이 추측이 맞았거나, 추측을 6회할 경우 화면에 게임이 끝났다는 message를 표시해주는 함수
### def game\_start()  
 게임이 끝난 후, Enter key를 눌러 게임을 재시작할 때, 변수 초기화 및 새로 Game screen을 생성해주는 함수
 이때 선택한 Mode에 따라서 Random하게 생성하는 단어가 달라진다. 
 Daily Mode의 경우 오늘의 날짜를 seed로 사용해 하루 내에는 항상 같은 Word만 생성한다.
 INF Mode의 경우 완전 Randomly하게 Word를 생성한다.
### def Hint()
 Hint를 클릭했을 때, Keyboard 부분의 Hint\_letter의 정보를 표시해주는 함수
### def check\_keyboard\_click()
 Keyboard 부분의 Click한 Letter을 입력해주는 함수
## words.py
 Player가 입력한 Word가 유효한지 확인할 수 있는 List가 담겨진 파일
# ToDo List
 * Score 기능 추가
 * Easy, Hard Mode 추가
 * INF Mode에서 실패 없이 연속 몇 문제 맞췄는지 알려주는 Message 구현
