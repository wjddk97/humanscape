# 원티드x위코드 백엔드 프리온보딩 과제5 :: 휴먼스케이프(Humanscape)

# 배포 주소 : 13.125.135.242

# 1. [TEAM] WithCODE

#### Members

| 이름   | github                         |
| ------ | ------------------------------ |
| 김민호 | https://github.com/maxkmh712   |
| 김주형 | https://github.com/BnDC        |
| 박치훈 | https://github.com/chihunmanse |
| 박현우 | https://github.com/Pagnim      |
| 이기용 | https://github.com/leeky940926 |
| 이정아 | https://github.com/wjddk97     |

------

# 2. 과제

#### [필수 포함 사항]

- READ.ME 작성
  - 프로젝트 빌드, 자세한 실행 방법 명시
  - 구현 방법과 이유에 대한 간략한 설명
  - 완료된 시스템이 배포된 서버의 주소
  - 해당 과제를 진행하면서 회고 내용 블로그 포스팅
- Swagger나 Postman을 이용하여 API 테스트 가능하도록 구현

#### [확인 사항]

- **ORM 사용 필수**
- **데이터베이스는 SQLite로 구현**
- secret key, api key 등을 레포지토리에 올리지 않도록 유의
  - [README.md](http://README.md) 에 관련 설명 명시 필요

#### [도전 과제]

- 배포하여 웹에서 사용 할 수 있도록 제공

- 임상정보 검색 API 제공

[과제 안내]

- 다음 사항들을 충족하는 서비스를 구현해주세요.
  - 임상정보를 수집하는 batch task
    - 참고: https://www.data.go.kr/data/3074271/fileData.do#/API 목록/GETuddi%3Acfc19dda-6f75-4c57-86a8-bb9c8b103887
  - 수집한 임상정보에 대한 API
    - 특정 임상정보 읽기(키 값은 자유)
  - 수집한 임상정보 리스트 API
    - 최근 일주일내에 업데이트(변경사항이 있는) 된 임상정보 리스트
      - pagination 기능
  - **Test 구현시 가산점이 있습니다.**

------

# 3. Skill & Tools

- **Skill :** [![img](https://camo.githubusercontent.com/0f3eb5f3e4c61d94657f16605ea420a0216673dfb085d100c458ed15be0599d2/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f507974686f6e2d3337373641423f7374796c653d666f722d7468652d6261646765266c6f676f3d507974686f6e266c6f676f436f6c6f723d7768697465)](https://camo.githubusercontent.com/0f3eb5f3e4c61d94657f16605ea420a0216673dfb085d100c458ed15be0599d2/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f507974686f6e2d3337373641423f7374796c653d666f722d7468652d6261646765266c6f676f3d507974686f6e266c6f676f436f6c6f723d7768697465) [![img](https://camo.githubusercontent.com/c4c1014e1f168ff271282b67ec9059c3cfc16b2a5cba6e0c7c98c3530f47f45c/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446a616e676f2d3039324532303f7374796c653d666f722d7468652d6261646765266c6f676f3d446a616e676f266c6f676f436f6c6f723d7768697465)](https://camo.githubusercontent.com/c4c1014e1f168ff271282b67ec9059c3cfc16b2a5cba6e0c7c98c3530f47f45c/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446a616e676f2d3039324532303f7374796c653d666f722d7468652d6261646765266c6f676f3d446a616e676f266c6f676f436f6c6f723d7768697465) [![img](https://camo.githubusercontent.com/9bf3ab62e0f872ed37f7d590e4577137b2dda11ffb0786f9b858cd39c2dc8c7f/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f73716c6974652d3039324532303f7374796c653d666f722d7468652d6261646765266c6f676f3d73716c697465266c6f676f436f6c6f723d23303033423537)](https://camo.githubusercontent.com/9bf3ab62e0f872ed37f7d590e4577137b2dda11ffb0786f9b858cd39c2dc8c7f/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f73716c6974652d3039324532303f7374796c653d666f722d7468652d6261646765266c6f676f3d73716c697465266c6f676f436f6c6f723d23303033423537)
- **Depoly :** [![img](https://camo.githubusercontent.com/9ad32f291fa1163a77cd2e919f8378b38bf66fd9de517178bf890e521178f341/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f415753204543322d3233324633453f7374796c653d666f722d7468652d6261646765266c6f676f3d416d617a6f6e20415753266c6f676f436f6c6f723d7768697465)](https://camo.githubusercontent.com/9ad32f291fa1163a77cd2e919f8378b38bf66fd9de517178bf890e521178f341/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f415753204543322d3233324633453f7374796c653d666f722d7468652d6261646765266c6f676f3d416d617a6f6e20415753266c6f676f436f6c6f723d7768697465) [![img](https://camo.githubusercontent.com/fbef20533fc559c07dcaae57d63beab86709421dfd5428391a563096c88ead5a/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f636b65722d3234393645443f7374796c653d666f722d7468652d6261646765266c6f676f3d446f636b6572266c6f676f436f6c6f723d7768697465)](https://camo.githubusercontent.com/fbef20533fc559c07dcaae57d63beab86709421dfd5428391a563096c88ead5a/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f636b65722d3234393645443f7374796c653d666f722d7468652d6261646765266c6f676f3d446f636b6572266c6f676f436f6c6f723d7768697465)
- **ETC :** [![img](https://camo.githubusercontent.com/fdb91eb7d32ba58701c8e564694cbe60e706378baefa180dbb96e2c1cfb9ec0f/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4769742d4630353033323f7374796c653d666f722d7468652d6261646765266c6f676f3d476974266c6f676f436f6c6f723d7768697465)](https://camo.githubusercontent.com/fdb91eb7d32ba58701c8e564694cbe60e706378baefa180dbb96e2c1cfb9ec0f/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4769742d4630353033323f7374796c653d666f722d7468652d6261646765266c6f676f3d476974266c6f676f436f6c6f723d7768697465) [![img](https://camo.githubusercontent.com/23a917c56e310800a66c58a03447dd42c0dea2abff415ef9719e3e837c1cff82/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4769746875622d3138313731373f7374796c653d666f722d7468652d6261646765266c6f676f3d476974687562266c6f676f436f6c6f723d7768697465)](https://camo.githubusercontent.com/23a917c56e310800a66c58a03447dd42c0dea2abff415ef9719e3e837c1cff82/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4769746875622d3138313731373f7374796c653d666f722d7468652d6261646765266c6f676f3d476974687562266c6f676f436f6c6f723d7768697465) [![img](https://camo.githubusercontent.com/879423585ed087f3c973857c43ba7e7d84f52c993d2c937055726339fbf921d9/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f506f73746d616e2d4646364333373f7374796c653d666f722d7468652d6261646765266c6f676f3d506f73746d616e266c6f676f436f6c6f723d7768697465)](https://camo.githubusercontent.com/879423585ed087f3c973857c43ba7e7d84f52c993d2c937055726339fbf921d9/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f506f73746d616e2d4646364333373f7374796c653d666f722d7468652d6261646765266c6f676f3d506f73746d616e266c6f676f436f6c6f723d7768697465)

------

# 4. 모델링


<img width="957" alt="스크린샷 2021-11-16 오후 10 07 21" src="https://user-images.githubusercontent.com/61782539/141990762-5f9386d7-159c-4da7-8e92-290ff61206dd.png">



------

# 5. Postman API 테스트

### API 테스트 : https://www.postman.com/cloudy-robot-203980/workspace/humanscape

### 기본 주소는 배포주소로 되어 있으며, 콜렉션 fork 후 테스트 부탁드립니다.

### API 명세서 : https://documenter.getpostman.com/view/17666851/UVC9hkgs

------

# 6. 구현 사항 상세 설명
## 1. GET /researches/{int:research_id} (특정 임상과제 조회)
- [성공] path parameter로 임상과제 id값을 받아와서 해당 임상과제 정보를 조회합니다. ex) /researches/

![image](https://user-images.githubusercontent.com/79758688/141976381-1f22e6b4-a8c7-4696-b775-29019912c4d3.png)

- [실패] 만약 존재하지 않는 임상과제 id값을 입력할 경우 404 code를 반환해줍니다.

![image](https://user-images.githubusercontent.com/79758688/141976696-499569b9-922f-443b-aa08-bbc4cfa8e049.png)

## 2. GET /researches (전체 임상과제 리스트 조회)
- [성공] path parameter를 입력하지 않을 경우 전체 임상과제 리스트를 조회합니다. pagination을 20으로 주어 데이터를 20개씩 조회하도록 하였습니다. 

![image](https://user-images.githubusercontent.com/79758688/141977141-76fe2717-9017-4ae5-9396-74763281f65e.png)

## 3. GET /researches?search=당뇨 (과제명으로 검색)
- [성공] 임상과제 검색 API를 구현했습니다. 먼저 search라는 변수를 데이터로 받아서 검색 기능을 추가했습니다. 검색 필터는 임의로 '과제명'과 '기관명'으로 설정하였습니다.  '당뇨'라는 필터로 검색 시 '과제명'에 '당뇨'가 포함되는 데이터들이 조회됩니다.

![image](https://user-images.githubusercontent.com/79758688/141977978-cde01a72-4558-4cb3-a36e-f1b82add3fd6.png)

## 4. GET /researches?search=서울성모 (기관명으로 검색)
- '서울성모' 라는 필터로 검색시 '연구기관'에 '서울성모'가 포함된 데이터들이 조회됩니다. 

![image](https://user-images.githubusercontent.com/79758688/141978271-071bad28-b300-4bcd-ad6b-0e8f2dc5aea1.png)

## 5. Batch task

![image](https://user-images.githubusercontent.com/75020336/142137760-f1dae3b4-89f1-4f46-ab02-fb81ab3dc2ef.png)


- 계속해서 업데이트가 필요한 코드는 django에서 지원해주는 django-crontab을 통하여 batch task를 구현하였습니다.

```
CRONJOBS = [
    ('* */4 * * *', 'researches.cron.batch_task', '>> ~/humanscape/cron.log 2>&1'),
]
```
- 4시간 마다 researches app에 있는 cron.py파일의 batch_task함수가 실행되고 에러 로그는 cron.log에 기록되도록 하였습니다.

## 5-1. 기능
- 외부 api를 가져오면 기존에 있는 데이터베이스의 값과 비교하여 새로 들어온 연구는 추가해주었습니다.
- 변경사항이 없는 연구는 값이 들어와도 변하지 않고 변경사항이 있는 정보는 데이터베이스에서 업데이트 해주고 update_at시간을 주었습니다.
- 
------

# 7. UnitTest 결과

<img width="779" alt="스크린샷 2021-11-16 오후 6 39 48" src="https://user-images.githubusercontent.com/79758688/141960630-899f8ebb-d097-4380-9812-c1db2983e230.png">


# 8 . Reference

이 프로젝트는 원티드x위코드 백엔드 프리온보딩 과제 일환으로 휴먼스케이프(humanscape)에서 출제한 과제를 기반으로 만들었습니다. 감사합니다.

