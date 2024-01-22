# Project ABC

* 맞춤형 음료 추천, 광고 시스템
* 1. 사람의 성별, 나이, 표정을 인식한 뒤, 추천 AI를 이용해 그에 맞는 음료의 광고를 추천해 준다.
  2. 광고를 보는 사람의 시선을 트래킹한 뒤 광고를 끝까지 시청하면 광고에 나온 음료를 권해준다.

## High Level Design

* usecase
  ![usecase](https://github.com/chansol1604/project_Ai_ad/assets/58240527/169f2348-a2bc-4239-9a77-68047309c2d1)
  
* sequence diagram
 ![sequence](https://github.com/chansol1604/project_Ai_ad/assets/58240527/2bf76bbb-0b2e-463c-9976-38c57e8883a2)
  
* class diagram
  ![class](https://github.com/chansol1604/project_Ai_ad/assets/58240527/74669d7e-e842-4d16-bed4-ce95ea4bcdeb)


  
## Clone code

* (각 팀에서 프로젝트를 위해 생성한 repository에 대한 code clone 방법에 대해서 기술)

```shell
git clone https://github.com/chansol1604/project_Ai_ad.git
```

## Prerequite

* (프로잭트를 실행하기 위해 필요한 dependencies 및 configuration들이 있다면, 설치 및 설정 방법에 대해 기술)

```shell
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Steps to build

* (프로젝트를 실행을 위해 빌드 절차 기술)

```shell
cd ~/xxxx
source .venv/bin/activate

make
make install
```

## Steps to run

* (프로젝트 실행방법에 대해서 기술, 특별한 사용방법이 있다면 같이 기술)

```shell
cd ~/xxxx
source .venv/bin/activate

cd /path/to/repo/xxx/
python demo.py -i xxx -m yyy -d zzz
```

## Output

* (프로젝트 실행 화면 캡쳐)


## Appendix

* (참고 자료 및 알아두어야할 사항들 기술)
