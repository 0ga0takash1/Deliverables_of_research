formated_array = [
    [
        "１．作業内容",
        ["本作業は、別添の「通関統計加工分析システムのクライアント・サーバ方式への移植作業」に係る仕様書に基づき同システムの基本設計、詳細設計、プログラム開発、システムテスト、ドキュメント作成ならびにコンテンツ作成を行うものである。 ",]
    ],
    [
        "２．納入物品",
        [
            [
                [
                    ["is table", "vertical", [10, 3]],
                    [
                        ["納入物品名", "納品数", "補足"],
                        ["① 基本設計書", "2 部（正、副）", "注 1"],
                        ["② 詳細設計書", "2 部（正、副）", "〃"],
                        ["③ プログラム説明書", "2 部（正、副）", "〃"],
                        ["④ 運用手順書", "2 部（正、副）", "〃"],
                        ["⑤ 操作説明書", "2 部（正、副）", "〃"],
                        ["⑥ コンテンツ作成報告書", "2 部（正、副）", "〃"],
                        ["⑦ テスト結果報告書", "2 部（正、副）", "〃"],
                        ["⑧ プログラム", "1 式", "注 2"],
                        ["⑨ データ", "", "注 3"],
                    ]
                ],
                "注 1  ①～⑦までの納入物品については、紙媒体および電子ファイル（一太郎 Ver.  9.0 以前又は Microsoft Word 98 以前の形式）で保存した CD-ROM 又は MO で納品すること。",
                "注 2  ⑧プログラムには、ソースプログラム、実行形式プログラム、利用環境等を定義するファイル、コンテンツを含めること。",
                "また、担当職員の指定するハードディスクおよび CD-ROM 等に格納すること。",
                "注 3  ⑨については、担当職員が指定するハードディスクおよび CD-ROM 等に格納すること。",
            ]
        ]
    ],
    [
        "３．納入期限",
        ["平成○○年○○月○○日（○）",]
    ],
    [
        "４．納入場所",
        ["経済産業省大臣官房情報システム厚生課",]
    ],
    [
        "５．システム開発条件",
        [
            "本システムの稼働・開発環境は以下のとおりである。",
            [
                "（１）  全体構成",
                [
                    "・本システムは、経済産業省の省内 PC-LAN に接続された一般執務用パソコン、開発用パソコン、および個別業務用イントラネットサーバより構成される。",
                    "・本システムはクライアント・サーバ方式で稼働すること。",
                ]
            ],
            [
                "（２）  機器構成",
                [
                    [
                        "①   一般執務用パソコン",
                        [
                            [
                                ["is table", "vertical", [11, 2]],
                                [
                                    ["項目", "主な仕様"],
                                    ["機種", "富士通製F MV-5233NA/X"],
                                    ["ＣＰＵ", "MMX Pentium 233MHz"],
                                    ["メモリ", "96MB"],
                                    ["ハードディスク", "3.2GB"],
                                    ["基本ＯＳ", "Microsoft Windows NT Workstation Version 4.0"],
                                    ["Web ブラウザ", ["Microsoft Internet Explorer 5.0", "Netscape Communicator 4.06"]],
                                    ["接続可能機器", "FDD､CD-ROM(32倍速以上)、ネットワーク(100BASE-TX/10BASE-T)、MO、CD-R等"],
                                    ["開発言語", "C、C++、html、Java Script、SQL、CGI"],
                                    ["文字コード", "シフトJIS"],
                                    ["その他", "上記以外のソフトウェア、開発言語等を使用する場合には、あらかじめ担当職員の了解を得ること。"],
                                ]
                            ],
                        ]
                    ],
                    [
                        "②   開発用パソコン",
                        [
                            [
                                ["is table", "vertical", [11, 2]],
                                [
                                    ["項目", "主な仕様"],
                                    ["機種", "日本電気製 Express5800/140Ha"],
                                    ["ＣＰＵ", "PentiumII 400MHz"],
                                    ["メモリ", "128MB"],
                                    ["ハードディスク", "8GB"],
                                    ["基本ＯＳ", "Microsoft Windows NT Workstation Version 4.0"],
                                    ["Web ブラウザ", ["Microsoft Internet Explorer 5.0", "Netscape Communicator 4.06"]],
                                    ["接続可能機器", "FDD ､ CD-ROM(32 倍 速 以 上 ) 、 ネ ッ ト ワ ー ク (100BASE-TX/10BASE-T"],
                                    ["開発言語", "C、C++、html、Java Script、SQL、CGI"],
                                    ["文字コード", "シフトJIS"],
                                    ["その他", "上記以外のソフトウェア、開発言語等を使用する場合には、あらかじめ担当職員の了解を得ること。"],
                                ]
                            ],
                        ]
                    ],
                    [
                        "③   個別業務用イントラネットサーバ",
                        [
                            [
                                ["is table", "vertical", [13, 2]],
                                [
                                    ["項目", "主な仕様"],
                                    ["機種", "日本電気製 Express5800/140Ha"],
                                    ["ＣＰＵ", "Intel PentiumII Xeon 400Mhz×4"],
                                    ["メモリ", "512MB"],
                                    ["ハードディスク", "9GB＋27GB(RAID)"],
                                    ["基本ＯＳ", "Microsoft Windows NT Server Enterprise Edition Version 4.0"],
                                    ["ミドルウェア等", ["Microsoft Internet Information Server 4.0", "Microsoft SQL Server 6.5 Enterprise Edition"]],
                                    ["Web ブラウザ", ["Microsoft Internet Explorer 5.0", "Netscape Communicator 4.06"]],
                                    ["ネットワーク", "100Mbps 対応イーサネットアダプタ"],
                                    ["接続可能機器", "FDD、MO、CD-ROM、DAT"],
                                    ["開発言語", "C、C++、html、Java Script、SQL、CGI"],
                                    ["文字コード", "シフトJIS"],
                                    ["その他", "上記以外のソフトウェア、開発言語等を使用する場合には、あらかじめ担当職員の了解を得ること。"],
                                ]
                            ],
                        ]
                    ],
                ]
            ],
            [
                "（３）  ネットワーク環境",
                [
                    "・ 当省の PC-LAN 環境において、TCP/IP を利用すること。",
                    "・ ネットワークトラフィックの効率化を図るために、冗長なトラフィックを発生させないようにすること。",
                ]
            ],
        ]
    ],
    [
        "６．その他",
        [
            [
                "(1)  信頼性等要件",
                ["別添「5.信頼性等要件」を参照のこと。"]
            ],
            [
                " (2) 作業の体制および方法",
                ["別添「7. 作業の体制および方法」を参照のこと。"]
            ],
            [
                " (3) 特記事項",
                [
                    "・省内で取り扱うデータおよび省内の情報システムの取扱いには十分注意を払い、省外に持ち出すことのないよう省内で作業を行うこと。",
                    "・契約期間中及び契約終了後においても、作業に関して知り得た当省の業務上の内容について、他に漏らし又は他の目的に利用してはならない。",
                    "・納入物品に関する著作権その他の知的所有権は、経済産業省に帰属するものとする。",
                    "・本システムの検索機能等により一時ファイルを作成する場合、又は、設定された作業ファイルを利用する場合は、資源が有効に活用できるよう配慮したシステムとすること。",
                    "また不必要な一時ファイル等は削除すること。",
                    "・本システムは、ネットワークを介して処理を行うため、ネットワークによる障害及びアプリケーションによる障害、利用者による中断に対して十分考慮して開発すること。",
                    "・特定の日付が原因となって発生するトラブルについて対応しており、いかなる日付においてもシステムが支障なく稼働すること。 ",
                    "・作業に際して発生した不明な点は、担当職員の指示に従うこと。",
                ]
            ]
        ]
    ],
    [
        "１． 作業の概要", 
        [
            ["（１）  目的", ["本開発は、現在、日本電気株式会社製の汎用電子計算機（ACOS PX7900/40）で稼働している「通関統計加工分析システム」（以下「現システム」と言う）を、当省が指定するサーバに移植し、汎用電子計算機上での処理と同様の結果を得られるようにすることを目的とする。"]],
            ["（２）  対象業務の概要", ["毎月財務省から CT で提供される通関統計と平成７年基準の工業統計（甲／乙）、CCCN-HS コード変換ファイル、ドル換算レート（毎月端末より入力）をもとに、国別表・基準表の 2 種類につき、それぞれドルベース・円ベース別、輸入・輸出別の合計 8 種類の帳票を作成する業務である。"]],
            ["（３）  システム化の範囲", ["本作業では、1.（2）で説明した業務のうち、通関統計加工分析システムの移植に係るシステム化を対象範囲とする。"]],
            ["（４）  作業の範囲", ["対象業務の内容や手順等を変更することなく、現システムをクライアント・サーバ方式で処理するようにシステムを開発するとともに、システムの稼働に必要なコンテンツを作成する。"]],
        ],
    ],
    [
        "２． システム開発",
        [
            [
                "（１）  システム機能",
                [
                    [
                        "①   システム機能一覧",
                        [
                            [
                                ["is table", "vertical", [5, 2]],
                                [
                                    ["機能名", "機能概要"],
                                    ["現状確認", "通関統計加工分析データ、工業統計加工分析データの作成状況を表示する。"],
                                    ["データ作成更新", "通関統計加工分析データおよび工業統計加工分析データの作成・更新を行う。"],
                                    ["国別表作成", "国別表の閲覧、印刷、CSV 出力を行う。"],
                                    ["基準表作成", "基準表の閲覧、印刷、CSV 出力を行う。"]
                                ]
                            ],
                        ]
                    ],
                    [
                        "②   システム機能の説明",
                        [
                            [
                                ["is table", "vertical", [5, 2]],
                                [
                                    ["機能名", "機能概要"],
                                    ["現状確認", [
                                                    "利用者の指示によって、通関統計加工分析データや工業統計加工分析データの作成状況を表示する。", 
                                                    "体的には以下の要件を満たすこと。", 
                                                    "・作成状況として作成日、通関統計データファイル生成日、工業統計データ（甲）ファイル作成日、工業統計データ（乙）ファイル作成日を含むこと。",
                                                    "・作成履歴を表示すること",
                                                ]
                                    ],
                                    ["データ作成更新", [
                                                        "利用者の指示によって、通関統計データファイル、工業統計データ（甲）ファイル、工業統計データ（乙）ファイル、CCCN－HS コード変換ファイルを読み込み、また、利用者の入力するドル換算レートを読み込み、通関統計加工分析データと工業統計加工分析データを生成する。",
                                                        "また、生成したデータを通関統計加工分析用データベースに登録する。",
                                                    ]
                                    ],
                                    ["国別表作成", [
                                                    "利用者の指示によって、通関統計加工分析ベースを読み込み、国別表を作成する。",
                                                    "具体的には以下の要件を満たすこと。 ",
                                                    "・国別表は CSV 形式のファイルとして出力できること",
                                                    "・国別表は印刷できること",
                                                    "・ドル建て／円立て、輸入／輸出の区分で国別表を作成すること。",
                                                    "・品目合計、品目詳細の区分で国別表を作成すること。",
                                                ]
                                    ],
                                    ["基準表作成", [
                                                    "利用者の指示によって、通関統計加工分析ベースを読み込み、基準表を作成する。",
                                                    "具体的には以下の要件を満たすこと。",
                                                    "・基準表は CSV 形式のファイルとして出力できること",
                                                    "・基準表は印刷できること",
                                                    "・ドル建て／円立て、輸入／輸出の区分で基準表を作成すること。",
                                                ]
                                    ]
                                ]
                            ],
                        ]
                    ],
                ]
            ],
            [
                "（２）  画面要件",
                [
                    [
                        "①   画面一覧",
                        [
                            [
                                ["is table", "vertical", [8, 2]],
                                [
                                    ["画面名", "画面概要"],
                                    ["ログイン画面", "本システムにログインする画面。"],
                                    ["初期画面", "どの機能を利用するか指示する画面。"],
                                    ["工業統計加工分析データ作成状況画面", "工業統計加工分析データの作成を指示する画面。"],
                                    ["工業統計加工分析データ作成画面", "工業統計加工分析データの作成を指示する画面。"],
                                    ["通関統計加工分析データ作成状況画面", "通関統計加工分析データの作成状況を表示する画面。"],
                                    ["通関統計加工分析データ作成画面", "通関統計加工分析データの作成を指示する画面。"],
                                    ["国別表・基準表作成画面", "国別表や基準表の作成を指示する画面。"]
                                ]
                            ],
                            "画面遷移は以下の通りである。",
                        ]
                    ],
                    [
                        "②   画面入出力要件",
                        [
                            [
                                ["is table", "vertical", [8, 2]],
                                [
                                    ["画面名", "入出力項目"],
                                    ["ログイン画面", "ID、パスワード"],
                                    ["初期画面", "利用可能機能、利用者の指示"],
                                    ["工業統計加工分析データ作成状況画面", "最新処理年月"],
                                    ["工業統計加工分析データ作成画面", "最新処理年月"],
                                    ["通関統計加工分析データ作成状況画面", "処理対象年月"],
                                    ["通関統計加工分析データ作成画面", "処理対象年月"],
                                    ["国別表・基準表作成画面", "作成対象表名、ドル／円区分、輸入／輸出区分"]
                                ]
                            ],
                        ]
                    ],
                ]
            ],
            [
                "（３）  帳票要件",
                [
                    [
                        "①   帳票一覧",
                        [
                            [
                                ["is table", "vertical", [4, 2]],
                                [
                                    ["帳票名", "帳票概要"],
                                    ["国別表", "国・地域毎の品目ごとの輸出入額"],
                                    ["基準表（品目合計）", "品目ごとの企業性との出荷額と構成比および構成比に対応した輸出入額"],
                                    ["基準表（品目詳細）", "詳細品目ごとの企業性との出荷額と構成比および構成比に対応した輸出入額"]
                                ]
                            ]
                        ]
                    ],
                    [
                        "②   帳票入出力要件",
                        [
                            [
                                ["is table", "vertical", [4, 2]],
                                [
                                    ["帳票名", "入出力項目"],
                                    ["国別表", "国・地域名、企業性、輸出入額"],
                                    ["基準表（品目合計）", "品目、企業性、出荷額、構成比、輸出入額"],
                                    ["基準表（品目詳細）", "品目詳細、企業性、出荷額、構成比、輸出入額"]
                                ]
                            ]
                        ]
                    ]
                ]
            ],
            [
                "（４）  データベース要件",
                [
                    [
                        "①   データベース一覧",
                        [
                            [
                                ["is table", "vertical", [2, 2]],
                                [
                                    ["データベース名", "概要"],
                                    ["通関統計加工分析用データベース", "通関統計加工分析を行うために必要なデータを集積したもの"]
                                ]
                            ]
                        ]
                    ],
                    [
                        "②   データベース要件",
                        [
                            [
                                ["is table", "vertical", [2, 2]],
                                [
                                    ["データベース名", "主要項目"],
                                    ["通関統計加工分析用データベース", [
                                                                    "次のファイルの全項目を含む。",
                                                                    [
                                                                        "―通関統計データファイル",
                                                                        "―工業統計（甲）調査データファイル",
                                                                        "―工業統計（乙）調査データファイル",
                                                                        "―CCCN-HS コード変換ファイル"
                                                                    ],
                                                                ]
                                    ]
                                ]
                            ],
                        ]
                    ],
                ]
            ],
            [
                "（５）  外部インタフェース要件",
                [
                    [
                        "①   外部インタフェース一覧",
                        [
                            [
                                ["is table", "vertical", [5, 2]], 
                                [
                                    ["インタフェース名", "概要"],
                                    ["通関統計データファイル", "財務省から毎月受領する通関統計のデータ。"],
                                    ["工業統計（甲）調査データファイル", "構造統計課から５年に一度受領する工業統計（甲）調査の結果データ。"],
                                    ["工業統計（乙）調査データファイル", "構造統計課から５年に一度受領する工業統計（乙）調査の結果データ"],
                                    ["CCCN-HSコード変換ファイル", "CCCNコードとHSコードの対応関係を示すデータ。年に１回中小企業庁調査課が作成する。"],
                                ]  
                            ]
                        ]
                    ],
                    [
                        "②   外部インタフェース要件",
                        [
                            [
                                ["is table", "vertical", [5, 2]], 
                                [
                                    ["インタフェース名", "主要項目"],
                                    ["通関統計データファイル", "別紙１のとおり。"],
                                    ["工業統計（甲）調査データファイル", "別紙２のとおり。"],
                                    ["工業統計（乙）調査データファイル", "別紙３のとおり。"],
                                    ["CCCN-HSコード変換ファイル", "CCCNコード、HSコード"],
                                ]  
                            ]
                        ]
                    ],
                ]
            ]
        ]
    ],
    [
        "３． コンテンツ作成",
        [
            [
                "（１）  コンテンツ",
                [
                    [
                        "①   コンテンツ一覧",
                        [
                            [
                                ["is table", "vertical", [2, 2]],
                                [
                                    ["コンテンツ名", "概要"],
                                    ["通関統計加工分析用データベース", "現システムが利用している通関統計加工分析用データベースと同一"],
                                ]
                            ],
                        ]
                    ],
                    [
                        "②   コンテンツの内容",
                        [
                            [
                                ["is table", "vertical", [2, 2]],
                                [
                                    ["コンテンツ名", "内容"],
                                    ["通関統計加工分析用データベース", "現システムが利用している通関統計加工分析用データベースと同一"],
                                ]
                            ],
                        ]
                    ],
                ]
            ],
            [
                "（２）  コンテンツ作成要件", 
                ["現システムが利用している通関統計加工分析用データベースに登録されている全てのデータを、本開発において構築されるデータベースに登録すること。"]
            ],
        ]
    ],
    [
        "４． 規模・性能要件",
        [
            [
                "（１）  規模要件",
                [
                    [
                        "①   対象機器設置場所",
                        ["本サイトで利用する機器は、経済産業省本省内に設置する。"]
                    ],
                    [
                        "②   利用者数",
                        [
                            "本サイトの利用者は、情報システム厚生課の担当者２～３名、中小企業庁調査課の担当者２～３名である。", 
                            "同時に利用するのは、上記のうち１名である。",
                        ]
                    ],
                    [
                        "③   データ量",
                        [
                            [
                                ["is table", "vertical", [5, 2]],
                                [
                                    ["名称", "データ量"],
                                    ["通関統計データファイル", "○○件"],
                                    ["工業統計（甲）調査データファイル", "○○件"],
                                    ["工業統計（乙）調査データファイル", "○○件"],
                                    ["CCCN-HSコード変換ファイル", "○○件"],
                                ]
                            ],
                        ]
                    ],
                ]
            ],
            [
                "（２）  性能要件",
                [
                    "・多数の職員の利用に際し、快適な作業を実現できる処理速度を有すること。",
                    "・レスポンス時間の目標値は平常時３秒以内、ピーク時５秒以内とする。",
                ]
            ],
        ]
    ],
    [
        "５． 信頼性等要件",
        [
            [
                "（１）  信頼性",
                [
                    "・障害に伴うシステム停止は年１回以内とすること。",
                    "・受注者の瑕疵となる障害が発生した場合は、担当者からの連絡を受けてから３時間以内に回復できること。",
                    "・画面機能の一部変更は、サーバ側のパラメータファイルの修正のみで対応可能なこと。",
                    "・機能の一部変更や追加において、クライアント側の環境設定変更が必要となる場合、その作業は全て受注者の責任範囲とする。",
                    "・障害復旧の際、データ復旧はすべてバックアップデータのリストアで対応できること。",
                    "・システム内の機能や取扱データは、その機能やデータの利用権限を持つユーザのみが利用可能であること。",
                ]
            ],
            [
                "（２）  拡張性 ",
                [
                    "・将来、データ量、利用者数等が調達時に指定した量の5割増となっても、プログラムやファイル等の改修なく対応できるよう、データベースやファイル等の容量に余裕を持たせること。",
                    "・ 将来、本システムが他システムと接続する際のプロトコルは、TCP/IP を前提とすること。",
                ]
            ],
            [
                "（３）  上位互換性",
                [
                    "・OS、ミドルウェア等のベンダーからバージョンアップ情報が既に提供されている場合には、それにも対応できるようにシステムを構築すること。 ",
                    "・ なお、技術的な問題等がある場合には、対応の可否について担当職員と協議し、その指示に従うこと。",
                ]
            ],
            [
                "(4) アクセシビリティ",
                [
                    "・ アクセシビリティを確保するために、「障害者・高齢者等情報処理機器アクセシビリティ指針」（平成 12 年 6 月通商産業省）に従うこと。",
                ]
            ],
        ]
    ],
    [
        "６． システム稼働・開発環境",
        [
            [
                "（１）  全体構成",
                [
                    "・本システムは、経済産業省の省内 PC-LAN に接続された一般執務用パソコン、開発用パソコン、および個別業務用イントラネットサーバより構成される。",
                    "・本システムはクライアント・サーバ方式で稼働すること。",
                    "・以下に全体構成図を示す。",
                ]
            ],
            [
                "（２）  機器構成",
                [
                    [
                        "①   一般執務用パソコン",
                        [
                            [
                                ["is table", "vertical", [11, 2]],
                                [
                                    ["項目", "主な仕様"],
                                    ["機種", "富士通製F MV-5233NA/X"],
                                    ["ＣＰＵ", "MMX Pentium 233MHz"],
                                    ["メモリ", "96MB"],
                                    ["ハードディスク", "3.2GB"],
                                    ["基本ＯＳ", "Microsoft Windows NT Workstation Version 4.0"],
                                    ["Web ブラウザ", ["Microsoft Internet Explorer 5.0", "Netscape Communicator 4.06"]],
                                    ["接続可能機器", "FDD､CD-ROM(32倍速以上)、ネットワーク(100BASE-TX/10BASE-T)、MO、CD-R等"],
                                    ["開発言語", "C、C++、html、Java Script、SQL、CGI"],
                                    ["文字コード", "シフトJIS"],
                                    ["その他", "上記以外のソフトウェア、開発言語等を使用する場合には、あらかじめ担当職員の了解を得ること。"],
                                ]
                            ],
                        ]
                    ],
                    [
                        "②   開発用パソコン",
                        [
                            [
                                ["is table", "vertical", [11, 2]],
                                [
                                    ["項目", "主な仕様"],
                                    ["機種", "日本電気製 Express5800/140Ha"],
                                    ["ＣＰＵ", "PentiumII 400MHz"],
                                    ["メモリ", "128MB"],
                                    ["ハードディスク", "8GB"],
                                    ["基本ＯＳ", "Microsoft Windows NT Workstation Version 4.0"],
                                    ["Web ブラウザ", ["Microsoft Internet Explorer 5.0", "Netscape Communicator 4.06"]],
                                    ["接続可能機器", "FDD ､ CD-ROM(32 倍 速 以 上 ) 、 ネ ッ ト ワ ー ク (100BASE-TX/10BASE-T"],
                                    ["開発言語", "C、C++、html、Java Script、SQL、CGI"],
                                    ["文字コード", "シフトJIS"],
                                    ["その他", "上記以外のソフトウェア、開発言語等を使用する場合には、あらかじめ担当職員の了解を得ること。"],
                                ]
                            ],
                        ]
                    ],
                    [
                        "③   個別業務用イントラネットサーバ",
                        [
                            [
                                ["is table", "vertical", [13, 2]],
                                [
                                    ["項目", "主な仕様"],
                                    ["機種", "日本電気製 Express5800/140Ha"],
                                    ["ＣＰＵ", "Intel PentiumII Xeon 400Mhz×4"],
                                    ["メモリ", "512MB"],
                                    ["ハードディスク", "9GB＋27GB(RAID)"],
                                    ["基本ＯＳ", "Microsoft Windows NT Server Enterprise Edition Version 4.0"],
                                    ["ミドルウェア等", ["Microsoft Internet Information Server 4.0", "Microsoft SQL Server 6.5 Enterprise Edition"]],
                                    ["Web ブラウザ", ["Microsoft Internet Explorer 5.0", "Netscape Communicator 4.06"]],
                                    ["ネットワーク", "100Mbps 対応イーサネットアダプタ"],
                                    ["接続可能機器", "FDD、MO、CD-ROM、DAT"],
                                    ["開発言語", "C、C++、html、Java Script、SQL、CGI"],
                                    ["文字コード", "シフトJIS"],
                                    ["その他", "上記以外のソフトウェア、開発言語等を使用する場合には、あらかじめ担当職員の了解を得ること。"],
                                ]
                            ],
                        ]
                    ],
                ]
            ],
            [
                "（３）  ネットワーク環境",
                [
                    "・ 当省の PC-LAN 環境において、TCP/IP を利用すること。",
                    "・ ネットワークトラフィックの効率化を図るために、冗長なトラフィックを発生させないようにすること。",
                ]
            ],
        ]
    ],
    [
        "７． 作業の体制および方法",
        [
            [
                "（１）  作業体制 ",
                [
                    [
                        "①   体制",
                        [
                            "受注者は、本作業を履行できる体制を設けると共に、作業に先立ち以下の事項について提出し、担当職員の了承を得ること。",
                            "なお、原則として体制の変更は認めず、やむを得ず変更する場合は事前に担当者の了承を得ること。",
                            "・  受注者側の体制",
                            "・  受注者側の責任者",
                            "・  連絡体制（受注者側の対応窓口）",
                        ]
                    ],
                    [
                        "②   主要担当者",
                        [
                            "・  主要担当者は、統計システムの企画・設計に関する知見や技術を有すること。",
                            "・  主要担当者は、Microsoft SQL Server を利用したシステム構築に関する知見や技術を有すること。",
                        ]
                    ],
                    [
                        "③   特記事項",
                        [
                            "・  省内で取り扱うデータおよび情報システムの取扱いには十分注意を払い、省外に持ち出すことのないよう省内で作業を行うこと。",
                            "・  担当職員が受注者に対し、常時契約履行状況に関する調査を行える体制とする",
                        ]
                    ],
                ]
            ],
            [
                "（２）  開発方法",
                [
                    [
                        "①   開発工程",
                        [
                            "・  受注者は、作業に先立ち開発スケジュールを書面で提出し、担当職員の了承を得ること。",
                            "・  やむを得ず作業スケジュール等を変更する場合は、事前に協議すること。",
                            "・  受注者はテストに先立ち「テスト計画書」を提出し、担当職員の了承を得ること。",
                            "なお、テスト計画書には、個別機能テストフェーズ、システム・テストフェーズ、実環境テストフェーズごとにテスト項目、テスト環境、テスト・シナリオをスケジュール表とともに明示すること。",
                        ]
                    ],
                    [
                        "②   ドキュメント",
                        [
                            "・  ドキュメントについては、作成に先立ちその構成や記載項目、記載内容および記載水準等を規定した作成要領を提出し、これに従うこと。",
                            "・  ドキュメントの内容について、担当職員のレビューを受けること。",
                        ]
                    ],
                    [
                        "③   進捗管理方法",
                        [
                            "・  原則として週１回、担当職員に対して進捗報告をすること。",
                            "・  進捗報告には、開発スケジュールと実際の進捗状況の差を明らかにし、その原因と対策を明らかにすること。",
                            "・  当省内での作業に当たっては担当職員の指示に従うものとし、作業終了後は報告書を提出するものとする。",
                        ]
                    ],
                    [
                        "④   開発環境の貸与",
                        [
                            "・  「6.システム稼働・開発環境」に示す環境を開発環境として使用することができる。",
                            "・  使用にあたっては、あらかじめ担当職員の了承を得ること。",
                            "・  使用する際には、当省の運用規則等に関する十分な知識を習得し、担当職員から与えられた環境下において作業を行うこと。",
                            "・  「6.システム稼働・開発環境」以外の開発環境は、受注者において手配すること。",
                            "・  システムテスト環境は、当省が用意する。",
                        ]
                    ],
                ]
            ],
            [
                "（３）  導入",
                [
                    "・  開発したシステムは、「6.システム稼働・開発環境」で利用することが可能となるように、導入作業を実施すること。",
                    "・  本システムの導入及び動作確認は、担当職員が指定する日時及び設置場所で実施すること。",
                    "・  動作確認にあたっては、あらかじめ計画書を提出し、これに従うこと。",
                ]
            ],
            [
                "（４）  利用者教育",
                [
                    "・  管理者が、本システムのエンドユーザ向け機能、システム管理機能を習得し、システムの管理・維持、ユーザサポートを行っていく上で必要な教育を実施すること。",
                ]
            ],
        ]
    ],
    [
        "８． 納品・検収",
        [
            [
                "（１）  納期",
                ["平成○○年○○月○○日（○）",]
            ],
            [
                "（２）  納入物品",
                [
                    [
                        ["is table", "vertical", [10, 3]],
                        [
                            ["納入物品名", "納品数", "補足"],
                            ["① 基本設計書", "2 部（正、副）", "注 1"],
                            ["② 詳細設計書", "2 部（正、副）", "〃"],
                            ["③ プログラム説明書", "2 部（正、副）", "〃"],
                            ["④ 運用手順書", "2 部（正、副）", "〃"],
                            ["⑤ 操作説明書", "2 部（正、副）", "〃"],
                            ["⑥ コンテンツ作成報告書", "2 部（正、副）", "〃"],
                            ["⑦ テスト結果報告書", "2 部（正、副）", "〃"],
                            ["⑧ プログラム", "1 式", "注 2"],
                            ["⑨ データ", "", "注 3"],
                        ]
                    ],
                    "注 1  ①～⑦までの納入物品については、紙媒体および電子ファイル（一太郎 Ver.  9.0 以前又は Microsoft Word 98 以前の形式）で保存した CD-ROM 又は MO で納品すること。",
                    "注 2  ⑧プログラムには、ソースプログラム、実行形式プログラム、利用環境等を定義するファイル、コンテンツを含めること。",
                    "また、担当職員の指定するハードディスクおよび CD-ROM 等に格納すること。",
                    "注 3  ⑨については、担当職員が指定するハードディスクおよび CD-ROM 等に格納すること。",
                ]
            ],
            [
                "（３）  納入場所",
                ["経済産業省大臣官房情報システム厚生課",]
            ],
            [
                "（４）  検収方法",
                [
                    [
                        "①   システムテスト",
                        [
                            "・  検収を受けるにあたっては、受注者は十分なテストを行ったうえで、当省が提供するテストデータを用い、当省が指定する場所においてシステムテストを実施すること。",
                            "・  システムテストの結果をテスト結果報告書として提出すること。",
                            "・  システムテスト時に使用した一時ファイル等の不要なファイル等は、システムテスト終了後、削除すること。",
                            "・  テスト結果報告書に対する指摘があった場合には、受注者は担当職員の指示に従い、適切な処置を施すこと。",
                        ]
                    ],
                    [
                        "②   完成検査",
                        [
                            "・  システムテスト終了後、担当職員が「（２）納入物品」の①〜⑦の記載内容内容を検査する。",
                            "・  これらの記載内容と⑧、⑨の内容との間に差異や矛盾点がないかを検査する。",
                            "・  完成検査において指摘があった場合には、担当職員の指示に従い、適切な処置を施すこと。"
                        ]
                    ],
                ]
            ],
        ]
    ],
]

# [[requirement], [candidate]]
    # [text, chapter, [other factors]]
to_html = [
    [[], []],
    [[], []],
    [[], []],
    [[], []],
    [[], []],
    [[], []],
    [[], []],
    [[], []],
    [[], []],
    [[], []],
    [[], []],
    [[], []],
    [[], []],
]

to_html[2][0].append([
    '本サイトの利用者は、情報システム厚生課の担当者２～３名、中小企業庁調査課の担当者２～３名である。同時に利用するのは、上記のうち１名である。',
    ['4. 規模・性能要件', '(1) 規模要件', '② 利用者数'],
    []    
])

to_html[2][0].append([
    '多数の職員の利用に際し、快適な作業を実現できる処理速度を有すること。',
    ['4. 規模・性能要件', '(2) 性能要件'],
    []
])

to_html[2][0].append([
    'レスポンス時間の目標値は平常時３秒以内、ピーク時５秒以内とする。',
    ['4. 規模・性能要件', '(2) 性能要件'],
    []
])

to_html[3][0].append([
    '現システムが利用している通関統計加工分析用データベースに登録されている全てのデータを、本開発において構築されるデータベースに登録すること。',
    ['3. コンテンツ作成', '(2) コンテンツ作成要件'],
    []
])

to_html[4][0].append([
    '本システムは、経済産業省の省内PC-LANに接続された一般執務用パソコン、開発用パソコン、および個別業務用イントラネットサーバより構成される。',
    ['6. システム稼働・開発環境', '(1) 全体構成'],
    []
])

to_html[4][0].append([
    '本システムはクライアント・サーバ方式で稼働すること。',
    ['6. システム稼働・開発環境', '(1) 全体構成'],
    []
])

to_html[4][0].append([
    '当省のPC-LAN環境において、TCP/IPを利用すること。',
    ['6. システム稼働・開発環境', '(3) ネットワーク環境'],
    []
])

to_html[4][0].append([
    'ネットワークトラフィックの効率化を図るために、冗長なトラフィックを発生させないようにすること。',
    ['6. システム稼働・開発環境', '(3) ネットワーク環境'],
    []
])

to_html[7][0].append([
    'OS、ミドルウェア等のベンダーからバージョンアップ情報が既に提供されている場合には、それにも対応できるようにシステムを構築すること。',
    ['５. 信頼性等要件', '(3) 上位互換性'],
    [12]
])

to_html[8][1].append([
    'アクセシビリティを確保するために、「障害者・高齢者等情報処理機器アクセシビリティ指針」（平成12年6月通商産業省）に従うこと。',
    ['5. 信頼性等要件', '(4) アクセシビリティ'],
    []
])

to_html[9][0].append([
    '本システムは、ネットワークを介して処理を行うため、ネットワークによる障害及びアプリケーションによる障害、利用者による中断に対して十分考慮して開発すること。',
    ['6. その他', '(3) 特記事項'],
    []
])

to_html[9][0].append([
    '特定の日付が原因となって発生するトラブルについて対応しており、いかなる日付においてもシステムが支障なく稼働すること。',
    ['6. その他', '(3) 特記事項'],
    []
])

to_html[9][0].append([
    '障害に伴うシステム停止は年１回以内とすること。',
    ['５. 信頼性等要件', '(1) 信頼性'],
    []
])

to_html[9][0].append([
    '受注者の瑕疵となる障害が発生した場合は、担当者からの連絡を受けてから３時間以内に回復できること。',
    ['５. 信頼性等要件', '(1) 信頼性'],
    []
])

to_html[9][0].append([
    '画面機能の一部変更は、サーバ側のパラメータファイルの修正のみで対応可能なこと。',
    ['５. 信頼性等要件', '(1) 信頼性'],
    []
])

to_html[9][0].append([
    '障害復旧の際、データ復旧はすべてバックアップデータのリストアで対応できること。',
    ['５. 信頼性等要件', '(1) 信頼性'],
    []
])

to_html[10][0].append([
    'システム内の機能や取扱データは、その機能やデータの利用権限を持つユーザのみが利用可能であること。',
    ['５. 信頼性等要件', '(1) 信頼性'],
    []
])

to_html[12][0].append([
    '将来、データ量、利用者数等が調達時に指定した量の 5 割増となっても、プログラムやファイル等の改修なく対応できるよう、データベースやファイル等の容量に余裕を持たせること。',
    ['５. 信頼性等要件', '(2) 拡張性'],
    []
])

to_html[12][0].append([
    '将来、本システムが他システムと接続する際のプロトコルは、TCP/IP を前提とすること。',
    ['５. 信頼性等要件', '(2) 拡張性'],
    []
])

to_html[12][0].append([
    'OS、ミドルウェア等のベンダーからバージョンアップ情報が既に提供されている場合には、それにも対応できるようにシステムを構築すること。',
    ['５. 信頼性等要件', '(3) 上位互換性'],
    [7]
])

# print(to_html)