import random

import pandas as pd

import csv



for i in range(10000):

    Dat1 = random.randint(1, 2)
    Dat2 = random.randint(1,5)

    if Dat1 == 1:
        aDat1 = '남'

    if Dat1 == 2:
        aDat1 = '여'

    if Dat2 == 1:
        aDat2 = '10'

    if Dat2 == 2:
        aDat2 = '20'

    if Dat2 == 3:
        aDat2 = '30'

    if Dat2 == 4:
        aDat2 = '40'

    if Dat2 == 5:
        aDat2 = '50'

    
    

    if Dat1 == 1:

        if Dat2 == 1:
            
            Dat3 = random.choices(range(1, 16), weights = [0.0627681493672936,
                0.0551331208453993,
                0.0637642968404452,
                0.0714420078509175,
                0.0703854700857075,
                0.0595300018605514,
                0.0765228110118156,
                0.0608795536569384,
                0.0638386779678008,
                0.0685327493828752,
                0.0785174447246164,
                0.0719882768828153,
                0.0683847806382259,
                0.0713517147586421,
                0.0584608096980428,
                ])

        if Dat2 == 2:

            Dat3 = random.choices(range(1, 16), weights = [0.0657821019872812,
                0.0592581247469462,
                0.0630046917947186,
                0.0702923815376959,
                0.0634059169597516,
                0.0632140684969385,
                0.074852150126817,
                0.062287121650228,
                0.0682043038724415,
                0.0646752292272346,
                0.0777825036207412,
                0.0703030072484579,
                0.0630373219301296,
                0.0720782539488372,
                0.063355172915837,
                ])

        if Dat2 == 3:

            Dat3 = random.choices(range(1, 16), weights = [0.0683813130607107,
                0.0597949020948737,
                0.0632168420584484,
                0.0686033676396161,
                0.0576745852050901,
                0.0662067111530585,
                0.0772689517710484,
                0.059897926402041,
                0.0694046577870895,
                0.0637539661596667,
                0.0776996249360647,
                0.0703298476265087,
                0.0601267891517921,
                0.0717448650690198,
                0.0673641001968152,
                ])

        if Dat2 == 4:

            Dat3 = random.choices(range(1, 16), weights = [0.0703778833277803,
                0.0586096379063641,
                0.0607185669252409,
                0.0693339094913768,
                0.0540709849003052,
                0.0700883033687725,
                0.0799619659504258,
                0.0585266471032016,
                0.0700883033687725,
                0.0606327723787283,
                0.0765399037335375,
                0.0709626974615519,
                0.0593016952232763,
                0.0731456920339267,
                0.0690224136051825,
                ])

        if Dat2 == 5:

            Dat3 = random.choices(range(1, 16), weights = [0.0674725697818134,
                0.0567842232552903,
                0.062591888044599,
                0.0708159634335072,
                0.0556797712370084,
                0.0711634870223563,
                0.0807949093737116,
                0.0597695421369635,
                0.0682521214645684,
                0.0603298003515907,
                0.0761037211469925,
                0.0689600962155938,
                0.0566795194169102,
                0.0760397486701611,
                0.0699234855955134,
                ])



    if Dat1 == 2:

        if Dat2 == 1:
            
            Dat3 = random.choices(range(1, 16), weights = [0.0636184208065262,
                0.0554597606182846,
                0.0645659766930913,
                0.0718924846123371,
                0.0690525483992113,
                0.0577663818886792,
                0.0770508214591891,
                0.0615156337363945,
                0.0672755716902199,
                0.0672206866857103,
                0.0793252628746846,
                0.0725866988295638,
                0.0653573706578053,
                0.0719704588761311,
                0.0568414031151666,
                ])

        if Dat2 == 2:

            Dat3 = random.choices(range(1, 16), weights = [0.0666267457014562,
                0.0595818543995329,
                0.0638077118755943,
                0.0707440176642228,
                0.0620522175771928,
                0.0614646160495402,
                0.0753821580891879,
                0.0629212436851683,
                0.0716081702491606,
                0.0633519092209684,
                0.0785916722608904,
                0.0709036896690087,
                0.0599739165028506,
                0.072695991891405,
                0.0617530089128028,
                ])

        if Dat2 == 3:

            Dat3 = random.choices(range(1, 16), weights = [0.0692211034652512,
                0.0601182530601444,
                0.064019487826681,
                0.0690567070881327,
                0.0563038240039473,
                0.064468767275471,
                0.0777960700999974,
                0.0605353720069084,
                0.0727994431054295,
                0.0624279576533547,
                0.0785089458698343,
                0.0709304940457157,
                0.0570437920018518,
                0.0723630647176241,
                0.0657760594301749,
                ])

        if Dat2 == 4:

            Dat3 = random.choices(range(1, 16), weights = [0.0712139456881417,
                0.0589338250554194,
                0.0615256205879149,
                0.0697865122094249,
                0.0526894960049228,
                0.0683652866241992,
                0.0804858643942025,
                0.0591660002719831,
                0.0734779166912851,
                0.0592976553670193,
                0.0773513557115125,
                0.0715624950311483,
                0.0562131441034453,
                0.0737619516950121,
                0.0674402149879853,
                ])

        if Dat2 == 5:

            Dat3 = random.choices(range(1, 16), weights = [0.068314057013732,
                0.0571096982034257,
                0.0633956364661332,
                0.071267071542735,
                0.0543030715986072,
                0.0694446050267518,
                0.0813178119140137,
                0.060407166335055,
                0.0716556260860248,
                0.0589937991838382,
                0.0769159746317188,
                0.0695625798999582,
                0.0535733175969909,
                0.0766520003888712,
                0.0683444614067445,
                ])

    Dat3 = Dat3[0]


    print(aDat1,aDat2, Dat3)



    file1 = open('./Datasets_02.csv','a', newline='')

    wr=csv.writer(file1)

    wr.writerow([aDat1, aDat2, Dat3])

    file1.close()




print('실행종료.')