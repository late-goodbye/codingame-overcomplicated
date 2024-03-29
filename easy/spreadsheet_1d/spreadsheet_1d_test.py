import unittest
from easy.spreadsheet_1d.spreadsheet_1d import Spreadsheet


def run_with_parameters(input_data, expected_output):
    def _format(data):
        return [int(x) for x in map(str.strip, data.split('\n')) if x]

    def inner_func(func):
        def wrapper(instance):
            spreadsheet = Spreadsheet(input_data)
            for cell_value, expected_value in zip(spreadsheet,
                                                  _format(expected_output)):
                instance.assertEqual(cell_value, expected_value)
        return wrapper
    return inner_func


class TestSpreadsheet(unittest.TestCase):
    @run_with_parameters(input_data='''
                            2
                            VALUE 3 _
                            ADD $0 4
                         ''',
                         expected_output='''
                            3
                            7
                         ''')
    def test_simple_dependency(self):
        pass

    @run_with_parameters(input_data='''
                            3
                            VALUE 20 _
                            ADD $0 100
                            ADD $1 1
                         ''',
                         expected_output='''
                            20
                            120
                            121
                         ''')
    def test_double_dependency(self):
        pass

    @run_with_parameters(input_data='''
                            2
                            VALUE 12 _
                            SUB $0 3
                         ''',
                         expected_output='''
                            12
                            9
                         ''')
    def test_subtraction(self):
        pass

    @run_with_parameters(input_data='''
                            2
                            VALUE 4 _
                            MULT 4 $0
                         ''',
                         expected_output='''
                            4
                            16
                         ''')
    def test_multiplication(self):
        pass

    @run_with_parameters(input_data='''
                            3
                            ADD 1 2
                            SUB 3 1
                            MULT 2 4
                         ''',
                         expected_output='''
                            3
                            2
                            8
                         ''')
    def test_no_dependencies(self):
        pass

    @run_with_parameters(input_data='''
                            7
                            VALUE 10 _
                            VALUE 3 _
                            MULT $0 $1
                            VALUE 2 _
                            VALUE 4 _
                            MULT $3 $4
                            ADD $2 $5   
                         ''',
                         expected_output='''
                            10
                            3
                            30
                            2
                            4
                            8
                            38
                         ''')
    def test_coefficients(self):
        pass

    @run_with_parameters(input_data='''
                            9
                            VALUE 0 _
                            VALUE 1 _
                            ADD $0 $1
                            ADD $1 $2
                            ADD $2 $3
                            ADD $3 $4
                            ADD $4 $5
                            ADD $5 $6
                            ADD $6 $7
                         ''',
                         expected_output='''
                            0
                            1
                            1
                            2
                            3
                            5
                            8
                            13
                            21
                         ''')
    def test_fibonacci(self):
        pass

    @run_with_parameters(input_data='''
                            2
                            ADD $1 20
                            VALUE 32 _
                         ''',
                         expected_output='''
                            52
                            32
                         ''')
    def test_backward_dependency(self):
        pass

    @run_with_parameters(input_data='''
                            4
                            SUB $1 4
                            VALUE 3 _
                            ADD 8 $1
                            MULT $0 $2
                         ''',
                         expected_output='''
                            -1
                            3
                            11
                            -11
                         ''')
    def test_diamond_dependency(self):
        pass

    @run_with_parameters(input_data='''
                            6
                            MULT $5 $2
                            ADD $5 $0
                            VALUE 12 _
                            ADD $2 $2
                            MULT $3 $2
                            SUB $3 $2
                         ''',
                         expected_output='''
                            144
                            156
                            12
                            24
                            288
                            12
                         ''')
    def test_accounting_is_easy(self):
        pass

    @run_with_parameters(input_data='''
                            100
                            SUB $47 $9
                            SUB 44 $59
                            ADD $97 $67
                            ADD $1 $1
                            SUB $57 $67
                            ADD $47 $97
                            ADD $59 $59
                            SUB $50 $83
                            SUB $3 $93
                            SUB $4 $74
                            SUB $38 $0
                            ADD $29 $96
                            SUB $46 $97
                            SUB $5 $98
                            SUB $87 $66
                            SUB $86 $25
                            SUB $1 $98
                            SUB $84 $56
                            ADD $38 $78
                            ADD $46 $34
                            ADD $5 $76
                            SUB $3 $93
                            ADD $19 $31
                            ADD $97 $77
                            VALUE $54 _
                            SUB $6 $6
                            ADD $98 $2
                            ADD $59 $67
                            SUB $36 $86
                            SUB $98 $26
                            SUB $16 $7
                            VALUE $67 _
                            ADD $11 $84
                            VALUE $63 _
                            ADD $3 $6
                            VALUE $44 _
                            SUB $68 $5
                            ADD $7 $58
                            ADD $50 $82
                            ADD $88 -936
                            ADD $43 $47
                            ADD $58 842
                            SUB $80 $46
                            SUB $33 $96
                            SUB $43 $46
                            ADD $2 $8
                            ADD $59 $9
                            VALUE $2 _
                            SUB $65 $30
                            ADD 135 $65
                            ADD $71 $93
                            ADD $96 $67
                            ADD $6 $38
                            SUB $5 $8
                            SUB $67 $1
                            ADD $4 $71
                            VALUE $67 _
                            SUB $93 $54
                            SUB $51 $3
                            ADD 993 -871
                            ADD $6 $6
                            SUB $71 $65
                            ADD $25 $60
                            VALUE $59 _
                            ADD $6 $51
                            SUB $63 $97
                            VALUE $67 _
                            SUB 3 $59
                            ADD $88 $3
                            SUB $83 $53
                            SUB $50 $49
                            ADD $60 865
                            VALUE $53 _
                            SUB $29 $44
                            SUB $96 $25
                            ADD $21 $77
                            SUB $14 $30
                            SUB $27 $50
                            ADD $51 $5
                            SUB $40 $72
                            VALUE $90 _
                            ADD $87 $42
                            ADD $9 $47
                            SUB $97 $1
                            ADD $21 $44
                            ADD $78 $94
                            ADD $21 $71
                            ADD -730 $67
                            SUB $21 $89
                            SUB $83 $25
                            ADD $47 $84
                            ADD $6 $65
                            ADD $32 $22
                            ADD $27 $59
                            ADD $63 $11
                            ADD $65 $60
                            ADD $59 $6
                            SUB $1 $27
                            ADD $27 $83
                            SUB $19 $61
                         ''',
                         expected_output='''
                            -119
                            -78
                            -200
                            -156
                            285
                            -281
                            244
                            1481
                            -281
                            -81
                            1316
                            566
                            122
                            -281
                            -730
                            1072
                            -78
                            -447
                            1163
                            129
                            548
                            -281
                            10
                            -1556
                            -41
                            0
                            -200
                            3
                            -1225
                            200
                            -1559
                            -119
                            0
                            122
                            88
                            -285
                            -153
                            1884
                            1197
                            -1214
                            -444
                            1245
                            -807
                            -244
                            -285
                            -481
                            41
                            -200
                            1762
                            338
                            1478
                            247
                            1441
                            0
                            -41
                            1638
                            -119
                            166
                            403
                            122
                            488
                            1150
                            488
                            122
                            491
                            203
                            -119
                            -119
                            -434
                            -3
                            1140
                            1353
                            0
                            485
                            366
                            -1756
                            829
                            -1475
                            -34
                            -444
                            -766
                            -1656
                            -281
                            -3
                            -566
                            654
                            1072
                            -849
                            -278
                            -3
                            -766
                            447
                            10
                            125
                            688
                            691
                            366
                            -81
                            0
                            -1021
                         ''')
    def test_accounting_is_hard_1(self):
        pass

    @run_with_parameters(input_data='''
                            100
                            MULT $61 $95
                            ADD $26 $80
                            ADD $6 $0
                            ADD $98 $39
                            ADD $72 $14
                            SUB $12 $32
                            MULT $73 $86
                            ADD $80 $12
                            MULT $86 $60
                            SUB $39 $59
                            SUB $64 $83
                            SUB $98 $91
                            SUB $59 $80
                            MULT $65 $73
                            ADD $25 $3
                            ADD $93 $10
                            SUB $93 $72
                            MULT $43 $23
                            MULT $43 $51
                            MULT $71 $0
                            SUB $60 $3
                            ADD $77 $46
                            SUB $23 $40
                            MULT $99 $6
                            MULT $44 $39
                            VALUE $28 _
                            VALUE $43 _
                            ADD $92 $46
                            ADD $49 $86
                            SUB $82 $41
                            ADD $12 $89
                            ADD $91 $86
                            SUB $60 $9
                            MULT $51 $3
                            SUB $12 $94
                            ADD $12 $28
                            ADD $66 $69
                            SUB $53 $1
                            ADD $98 $53
                            ADD $98 $98
                            ADD $42 $59
                            SUB $64 $0
                            SUB $98 $6
                            MULT 609 -14
                            ADD $60 $55
                            SUB $59 -245
                            MULT $64 $1
                            MULT $99 $98
                            ADD $46 $97
                            SUB $86 $43
                            MULT $28 $18
                            MULT $64 $40
                            SUB $70 $32
                            MULT $91 $80
                            ADD $83 $6
                            ADD $97 $76
                            MULT $23 $45
                            SUB $53 $22
                            MULT $6 $10
                            ADD $39 $98
                            MULT $17 $26
                            MULT $93 $59
                            SUB $70 $99
                            SUB $64 $43
                            SUB $9 $9
                            MULT $91 $53
                            MULT $26 $80
                            ADD $9 $43
                            SUB $72 $13
                            ADD $64 $82
                            ADD $80 $45
                            SUB $12 $61
                            ADD $53 $73
                            SUB $43 $98
                            MULT $47 $86
                            SUB $56 $99
                            SUB $53 $51
                            ADD 681 $43
                            ADD $70 $18
                            MULT $12 $51
                            MULT $6 $45
                            SUB $99 $40
                            VALUE $45 _
                            SUB $59 $98
                            SUB $6 $59
                            MULT $55 $51
                            SUB $39 $39
                            SUB $26 $73
                            ADD $84 $92
                            ADD $97 $50
                            SUB $75 $66
                            ADD $86 $43
                            MULT 295 $60
                            MULT $31 $17
                            SUB $9 $11
                            SUB $87 $65
                            MULT $64 $55
                            MULT $49 $23
                            MULT -6 380
                            VALUE $53 _
                         ''',
                         expected_output='''
                            0
                            -8526
                            0
                            -6840
                            -4560
                            -4560
                            0
                            -6840
                            0
                            2280
                            4560
                            6246
                            -6840
                            0
                            1686
                            4560
                            6246
                            0
                            0
                            0
                            6840
                            -7845
                            9120
                            0
                            0
                            8526
                            -8526
                            0
                            8526
                            -6595
                            -6840
                            -8526
                            -2280
                            0
                            -2874
                            1686
                            -6595
                            8526
                            -2280
                            -4560
                            -9120
                            0
                            -2280
                            -8526
                            0
                            -6595
                            0
                            0
                            0
                            8526
                            0
                            0
                            -4315
                            0
                            -4560
                            0
                            0
                            -9120
                            0
                            -6840
                            0
                            0
                            -6595
                            8526
                            0
                            0
                            0
                            -6246
                            -6246
                            -6595
                            -6595
                            -6840
                            -6246
                            -6246
                            0
                            0
                            0
                            -7845
                            -6595
                            0
                            0
                            9120
                            -6595
                            -4560
                            6840
                            0
                            0
                            -2280
                            6840
                            0
                            0
                            -8526
                            0
                            0
                            -3966
                            -2280
                            0
                            0
                            -2280
                            0
                         ''')
    def test_accounting_is_hard_2(self):
        pass

    @run_with_parameters(input_data='''
                            92
                            SUB $33 $64
                            ADD $60 $60
                            ADD $61 $61
                            SUB $76 $80
                            SUB $25 $59
                            ADD $58 $28
                            ADD $88 $59
                            ADD $32 $32
                            ADD $83 $21
                            ADD $69 $39
                            ADD $57 $64
                            ADD $26 $26
                            ADD $1 $1
                            SUB $62 $68
                            ADD $73 $1
                            ADD $50 $27
                            SUB $24 $2
                            ADD $14 $12
                            ADD $10 $89
                            SUB $67 $35
                            ADD $58 $58
                            ADD $7 $7
                            SUB $0 $89
                            ADD $20 $20
                            SUB $43 $61
                            SUB $53 $11
                            ADD $37 $37
                            ADD $82 $47
                            ADD $90 $2
                            ADD $89 $89
                            ADD $85 $85
                            SUB $91 $47
                            ADD $69 $69
                            SUB $46 $86
                            SUB $42 $20
                            ADD $12 $12
                            ADD $56 $8
                            ADD $72 $72
                            ADD $9 $32
                            ADD $30 $77
                            ADD $80 $48
                            ADD $79 $81
                            SUB $16 $58
                            SUB $44 $56
                            SUB $63 $21
                            ADD $20 $5
                            SUB $49 $81
                            ADD $54 $54
                            ADD $29 $18
                            SUB $34 $23
                            ADD $47 $47
                            SUB $74 $32
                            SUB $17 $72
                            SUB $71 $26
                            ADD $59 $59
                            ADD $15 $68
                            ADD $21 $21
                            ADD $86 $41
                            ADD $2 $2
                            ADD $11 $11
                            ADD $80 $80
                            ADD $56 $56
                            SUB $31 $50
                            SUB $51 $7
                            ADD $86 $86
                            ADD $72 $35
                            SUB $75 $30
                            SUB $70 $12
                            ADD $50 $50
                            ADD $30 $30
                            SUB $84 $1
                            SUB $52 $37
                            VALUE 1 _
                            ADD $40 $60
                            SUB $66 $69
                            SUB $13 $85
                            SUB $22 $29
                            ADD $55 $85
                            ADD $37 $65
                            ADD $23 $45
                            ADD $29 $29
                            ADD $23 $23
                            ADD $54 $6
                            ADD $38 $7
                            SUB $3 $60
                            ADD $68 $68
                            ADD $81 $81
                            ADD $78 $26
                            ADD $87 $11
                            ADD $64 $64
                            ADD $61 $36
                            SUB $4 $54
                         ''',
                         expected_output='''
                            2130706432
                            268435456
                            131072
                            2013265920
                            2147483616
                            1074266111
                            1073741855
                            8192
                            1073774591
                            1073745919
                            1090519039
                            8
                            536870912
                            2147483136
                            1610612735
                            1073742079
                            2147221504
                            2147483647
                            1107296255
                            0
                            524288
                            16384
                            2113929216
                            1048576
                            2147352576
                            2147483632
                            4
                            1073741951
                            1074003967
                            33554432
                            1024
                            2147483520
                            4096
                            2139095040
                            2146435072
                            1073741824
                            1073807359
                            2
                            1073750015
                            1073743871
                            1207959551
                            1077936127
                            2146959360
                            2147418112
                            2147450880
                            1074790399
                            2143289344
                            64
                            1140850687
                            2145386496
                            128
                            2147475456
                            2147483646
                            2147483640
                            32
                            1073742335
                            32768
                            1082130431
                            262144
                            16
                            134217728
                            65536
                            2147483392
                            2147467264
                            8388608
                            1073741825
                            2147481600
                            1073741824
                            256
                            2048
                            1610612736
                            2147483644
                            1
                            1342177279
                            2147479552
                            2147482624
                            2080374784
                            1073742847
                            1073741827
                            1075838975
                            67108864
                            2097152
                            1073741887
                            1073758207
                            1879048192
                            512
                            4194304
                            1073741831
                            1073741839
                            16777216
                            1073872895
                            2147483584
                         ''')
    def test_deep_recursion(self):
        pass


if __name__ == '__main__':
    unittest.main()
