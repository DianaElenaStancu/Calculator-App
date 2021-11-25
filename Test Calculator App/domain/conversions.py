from Calculator_App.domain.conversions import convert_din_baza_2, convert_in_baza_2, convert_rapid, convert_directa, convert_din_baza_10, \
    convert_in_baza_10, convert_impartiri, convert_substitutie, convert_intermediar

#convertire rapida
def test_convert_din_baza_2():
    assert (convert_din_baza_2("0", 4) == "0")
    assert (convert_din_baza_2("0", 8) == "0")
    assert (convert_din_baza_2("0", 16) == "0")
    assert (convert_din_baza_2("0101010111101", 4) == "222331")
    assert (convert_din_baza_2("111010101010111", 4) == "13111113")
    assert (convert_din_baza_2("0101010111101", 8) == "5275")
    assert (convert_din_baza_2("111010101010111", 8) == "72527")
    assert (convert_din_baza_2("0101010111101", 16) == "ABD")
    assert (convert_din_baza_2("111010101010111", 16) == "7557")

def test_convert_in_baza_2():
    assert (convert_in_baza_2("1223322010", 4) == "1101011111010000100")
    assert (convert_in_baza_2("12345670012", 8) == "1010011100101110111000000001010")
    assert (convert_in_baza_2("01023456789ABCDEF", 16) == "1000000100011010001010110011110001001101010111100110111101111")

def test_convert_rapid():
    assert (convert_rapid("0", 2, 4) == "0")
    assert (convert_rapid("0",2, 8) == "0")
    assert (convert_rapid("0",2, 16) == "0")
    assert (convert_rapid("0101010111101",2, 4) == "222331")
    assert (convert_rapid("111010101010111",2, 4) == "13111113")
    assert (convert_rapid("0101010111101",2, 8) == "5275")
    assert (convert_rapid("111010101010111",2, 8) == "72527")
    assert (convert_rapid("0101010111101",2, 16) == "ABD")
    assert (convert_rapid("111010101010111",2, 16) == "7557")
    assert (convert_rapid("0", 4, 2) == "0")
    assert (convert_rapid("0", 8, 2) == "0")
    assert (convert_rapid("0", 16, 2) == "0")
    assert (convert_rapid("1223322010", 4, 2) == "1101011111010000100")
    assert (convert_rapid("12345670012", 8, 2) == "1010011100101110111000000001010")
    assert (convert_rapid("01023456789ABCDEF", 16, 2) == "1000000100011010001010110011110001001101010111100110111101111")
    assert (convert_rapid("0101010111101", 2, 2) == "0101010111101")
    assert (convert_rapid("1223322010", 4, 4) == "1223322010")
    assert (convert_rapid("12345670012",8, 8) == "12345670012",)
    assert (convert_rapid("01023456789ABCDEF",16, 16) == "01023456789ABCDEF")
    assert (convert_rapid("01233302",4, 8)=="15762")
    assert (convert_rapid("01233302",4, 16) == "1BF2")
    assert (convert_rapid("1234555076", 8, 4) == "22130231220332")
    assert (convert_rapid("1234555076", 8, 16) == "A72DA3E")
    assert (convert_rapid("AA0F", 16, 4) == "22220033")
    assert (convert_rapid("AA0F", 16, 8) == "125017")

#conversie directa
def test_convert_impartiri():
    assert (convert_impartiri("123456770", 8, 3) == '1112020022002120')
    assert (convert_impartiri("02", 3, 2) == '10')
    assert (convert_impartiri("123450", 7, 2) == '101100101010101')
    assert (convert_impartiri("123450", 7, 3) == '1011101000')
    assert (convert_impartiri("123450", 7, 4) == '11211111')
    assert (convert_impartiri("123450", 7, 5) == '1212434')
    assert (convert_impartiri("123450", 7, 6) == '253513')

def test_convert_substitutie():
    assert (convert_substitutie("10001010101010101100", 2, 3) == '1001212010022')
    assert (convert_substitutie("10001010101010101100", 2, 4) == '2022222230')
    assert (convert_substitutie("10001010101010101100", 2, 5) == '121133410')
    assert (convert_substitutie("10001010101010101100", 2, 6) == '20101312')
    assert (convert_substitutie("10001010101010101100", 2, 7) == '4553630')
    assert (convert_substitutie("10001010101010101100", 2, 8) == '2125254')
    assert (convert_substitutie("10001010101010101100", 2, 9) == '1055108')
    assert (convert_substitutie("10001010101010101100", 2, 10) == '567980')
    assert (convert_substitutie("10001010101010101100", 2, 11) == '358806')
    assert (convert_substitutie("10001010101010101100", 2, 12) == '234838')
    assert (convert_substitutie("10001010101010101100", 2, 13) == '16B6AA')
    assert (convert_substitutie("10001010101010101100", 2, 14) == '10ADC0')
    assert (convert_substitutie("10001010101010101100", 2, 15) == 'B3455')
    assert (convert_substitutie("10001010101010101100", 2, 16) == '8AAAC')
    assert (convert_substitutie("02", 3, 4) == '2')
    assert (convert_substitutie("02", 3, 5) == '2')
    assert (convert_substitutie("02", 3, 6) == '2')
    assert (convert_substitutie("02", 3, 7) == '2')
    assert (convert_substitutie("02", 3, 8) == '2')
    assert (convert_substitutie("02", 3, 9) == '2')
    assert (convert_substitutie("02", 3, 10) == '2')
    assert (convert_substitutie("02", 3, 11) == '2')
    assert (convert_substitutie("02", 3, 12) == '2')
    assert (convert_substitutie("02", 3, 13) == '2')
    assert (convert_substitutie("02", 3, 14) == '2')
    assert (convert_substitutie("02", 3, 15) == '2')
    assert (convert_substitutie("02", 3, 16) == '2')
    assert (convert_substitutie("13320102", 4, 5) == '2013044')
    assert (convert_substitutie("13320102", 4, 6) == '405230')
    assert (convert_substitutie("13320102", 4, 7) == '163044')
    assert (convert_substitutie("13320102", 4, 8) == '77022')
    assert (convert_substitutie("13320102", 4, 9) == '48240')
    assert (convert_substitutie("13320102", 4, 10) == '32274')
    assert (convert_substitutie("13320102", 4, 11) == '22280')
    assert (convert_substitutie("13320102", 4, 12) == '16816')
    assert (convert_substitutie("13320102", 4, 13) == '118C8')
    assert (convert_substitutie("13320102", 4, 14) == 'BA94')
    assert (convert_substitutie("13320102", 4, 15) == '9869')
    assert (convert_substitutie("13320102", 4, 16) == '7E12')
    assert (convert_substitutie("13232443140012", 5, 6) == '542552155242')
    assert (convert_substitutie("13232443140012", 5, 7) == '102455646515')
    assert (convert_substitutie("13232443140012", 5, 8) == '17425076512')
    assert (convert_substitutie("13232443140012", 5, 9) == '5341008148')
    assert (convert_substitutie("13232443140012", 5, 10) == '2085911882')
    assert (convert_substitutie("13232443140012", 5, 11) == '98049651A')
    assert (convert_substitutie("13232443140012", 5, 12) == '4A2698B22')
    assert (convert_substitutie("13232443140012", 5, 13) == '2731C75B2')
    assert (convert_substitutie("13232443140012", 5, 14) == '15B05DD7C')
    assert (convert_substitutie("13232443140012", 5, 15) == 'C31D2E72')
    assert (convert_substitutie("13232443140012", 5, 16) == '7C547D4A')
    assert (convert_substitutie("123", 6, 7) == '102')
    assert (convert_substitutie("123", 6, 8) == '63')
    assert (convert_substitutie("123", 6, 9) == '56')
    assert (convert_substitutie("123", 6, 10) == '51')
    assert (convert_substitutie("123", 6, 11) == '47')
    assert (convert_substitutie("123", 6, 12) == '43')
    assert (convert_substitutie("123", 6, 13) == '3C')
    assert (convert_substitutie("123", 6, 14) == '39')
    assert (convert_substitutie("123", 6, 15) == '36')
    assert (convert_substitutie("123", 6, 16) == '33')
    assert (convert_substitutie("123450", 7, 8) == '54525')
    assert (convert_substitutie("123450", 7, 9) == '34330')
    assert (convert_substitutie("123450", 7, 10) == '22869')
    assert (convert_substitutie("123450", 7, 11) == '16200')
    assert (convert_substitutie("123450", 7, 12) == '11299')
    assert (convert_substitutie("123450", 7, 13) == 'A542')
    assert (convert_substitutie("123450", 7, 14) == '8497')
    assert (convert_substitutie("123450", 7, 15) == '6B99')
    assert (convert_substitutie("123450", 7, 16) == '5955')

def test_convert_directa():
    assert(convert_directa("10001010101010101100", 2, 3) == '1001212010022')
    assert(convert_directa("10001010101010101100", 2, 4) == '2022222230')
    assert(convert_directa("10001010101010101100", 2, 5) == '121133410')
    assert(convert_directa("10001010101010101100", 2, 6) == '20101312')
    assert(convert_directa("10001010101010101100", 2, 7) == '4553630')
    assert(convert_directa("10001010101010101100", 2, 8) == '2125254')
    assert(convert_directa("10001010101010101100", 2, 9) == '1055108')
    assert(convert_directa("10001010101010101100", 2, 10) == '567980')
    assert(convert_directa("10001010101010101100", 2, 11) == '358806')
    assert(convert_directa("10001010101010101100", 2, 12) == '234838')
    assert(convert_directa("10001010101010101100", 2, 13) == '16B6AA')
    assert(convert_directa("10001010101010101100", 2, 14) == '10ADC0')
    assert(convert_directa("10001010101010101100", 2, 15) == 'B3455')
    assert(convert_directa("10001010101010101100", 2, 16) == '8AAAC')
    assert (convert_directa("02", 3, 2) == '10')
    assert (convert_directa("02", 3, 4) == '2')
    assert (convert_directa("02", 3, 5) == '2')
    assert (convert_directa("02", 3, 6) == '2')
    assert (convert_directa("02", 3, 7) == '2')
    assert (convert_directa("02", 3, 8) == '2')
    assert (convert_directa("02", 3, 9) == '2')
    assert (convert_directa("02", 3, 10) == '2')
    assert (convert_directa("02", 3, 11) == '2')
    assert (convert_directa("02", 3, 12) == '2')
    assert (convert_directa("02", 3, 13) == '2')
    assert (convert_directa("02", 3, 14) == '2')
    assert (convert_directa("02", 3, 15) == '2')
    assert (convert_directa("02", 3, 16) == '2')
    assert (convert_directa("13320102", 4, 2) == '111111000010010')
    assert (convert_directa("13320102", 4, 3) == '1122021100')
    assert (convert_directa("13320102", 4, 5) == '2013044')
    assert (convert_directa("13320102", 4, 6) == '405230')
    assert (convert_directa("13320102", 4, 7) == '163044')
    assert (convert_directa("13320102", 4, 8) == '77022')
    assert (convert_directa("13320102", 4, 9) == '48240')
    assert (convert_directa("13320102", 4, 10) == '32274')
    assert (convert_directa("13320102", 4, 11) == '22280')
    assert (convert_directa("13320102", 4, 12) == '16816')
    assert (convert_directa("13320102", 4, 13) == '118C8')
    assert (convert_directa("13320102", 4, 14) == 'BA94')
    assert (convert_directa("13320102", 4, 15) == '9869')
    assert (convert_directa("13320102", 4, 16) == '7E12')
    assert (convert_directa("13232443140012", 5, 2) == '1111100010101000111110101001010')
    assert (convert_directa("13232443140012", 5, 3) == '12101101000022011122')
    assert (convert_directa("13232443140012", 5, 4) == '1330111013311022')
    assert (convert_directa("13232443140012", 5, 6) == '542552155242')
    assert (convert_directa("13232443140012", 5, 7) == '102455646515')
    assert (convert_directa("13232443140012", 5, 8) == '17425076512')
    assert (convert_directa("13232443140012", 5, 9) == '5341008148')
    assert (convert_directa("13232443140012", 5, 10) == '2085911882')
    assert (convert_directa("13232443140012", 5, 11) == '98049651A')
    assert (convert_directa("13232443140012", 5, 12) == '4A2698B22')
    assert (convert_directa("13232443140012", 5, 13) == '2731C75B2')
    assert (convert_directa("13232443140012", 5, 14) == '15B05DD7C')
    assert (convert_directa("13232443140012", 5, 15) == 'C31D2E72')
    assert (convert_directa("13232443140012", 5, 16) == '7C547D4A')
    assert (convert_directa("123", 6, 2) == '110011')
    assert (convert_directa("123", 6, 3) == '1220')
    assert (convert_directa("123", 6, 4) == '303')
    assert (convert_directa("123", 6, 5) == '201')
    assert (convert_directa("123", 6, 7) == '102')
    assert (convert_directa("123", 6, 8) == '63')
    assert (convert_directa("123", 6, 9) == '56')
    assert (convert_directa("123", 6, 10) == '51')
    assert (convert_directa("123", 6, 11) == '47')
    assert (convert_directa("123", 6, 12) == '43')
    assert (convert_directa("123", 6, 13) == '3C')
    assert (convert_directa("123", 6, 14) == '39')
    assert (convert_directa("123", 6, 15) == '36')
    assert (convert_directa("123", 6, 16) == '33')
    assert (convert_directa("123450", 7, 2) == '101100101010101')
    assert (convert_directa("123450", 7, 3) == '1011101000')
    assert (convert_directa("123450", 7, 4) == '11211111')
    assert (convert_directa("123450", 7, 5) == '1212434')
    assert (convert_directa("123450", 7, 6) == '253513')
    assert (convert_directa("123450", 7, 8) == '54525')
    assert (convert_directa("123450", 7, 9) == '34330')
    assert (convert_directa("123450", 7, 10) == '22869')
    assert (convert_directa("123450", 7, 11) == '16200')
    assert (convert_directa("123450", 7, 12) == '11299')
    assert (convert_directa("123450", 7, 13) == 'A542')
    assert (convert_directa("123450", 7, 14) == '8497')
    assert (convert_directa("123450", 7, 15) == '6B99')
    assert (convert_directa("123450", 7, 16) == '5955')
    assert (convert_directa("123456770", 8, 3) == '1112020022002120')
    assert (convert_directa("123456770", 8, 16) == '14E5DF8')
    assert (convert_directa("8736281548", 9, 5) == '24000102302101')
    assert (convert_directa("8736281548", 9, 15) == '15018E51B')
    assert (convert_directa("A34", 11, 7) == '3431')
    assert (convert_directa("A34", 11, 13) == '74C')
    assert (convert_directa("A3420B", 12, 8) == '11603453')
    assert (convert_directa("A3420B", 12, 13) == '6B7272')

#convertire cu baza 10 intermediar
def test_convert_din_baza_10():
    assert (convert_din_baza_10("1234567890", 2) == "1001001100101100000001011010010")
    assert (convert_din_baza_10("1234567890", 3) == "10012001001112202200")
    assert (convert_din_baza_10("1234567890", 4) == "1021211200023102")
    assert (convert_din_baza_10("1234567890", 5) == "10012022133030")
    assert (convert_din_baza_10("1234567890", 6) == "322301024030")
    assert (convert_din_baza_10("1234567890", 7) == "42410440203")
    assert (convert_din_baza_10("1234567890", 8) == "11145401322")
    assert (convert_din_baza_10("1234567890", 9) == "3161045680")
    assert (convert_din_baza_10("1234567890", 10) == "1234567890")
    assert (convert_din_baza_10("1234567890", 11) == "583977146")
    assert (convert_din_baza_10("1234567890", 12) == "2A5555016")
    assert (convert_din_baza_10("1234567890", 13) == "168A0865A")
    assert (convert_din_baza_10("1234567890", 14) == "B9D6B5AA")
    assert (convert_din_baza_10("1234567890", 15) == "735B7D60")
    assert (convert_din_baza_10("1234567890", 16) == "499602D2")

def test_convert_in_baza_10():
    assert (convert_in_baza_10("0110111001", 2) == "441")
    assert (convert_in_baza_10("0110222122212111001", 3) == "186356080")
    assert (convert_in_baza_10("01310222122212111033013", 4) == "8017002714055")
    assert (convert_in_baza_10("01310242212221211103301400003", 5) == "12253503767389871878")
    assert (convert_in_baza_10("01310242212221211103301400003500000000", 6) == "15779896525555477077606135552")
    assert (convert_in_baza_10("0131056500000000", 7) == "984414713163")
    assert (convert_in_baza_10("01310565777", 8) == "186838015")
    assert (convert_in_baza_10("0", 9) == "0")
    assert (convert_in_baza_10("110111001", 10) == "110111001")
    assert (convert_in_baza_10("A456", 11) == "13855")
    assert (convert_in_baza_10("A45B06", 12) == "2581494")
    assert (convert_in_baza_10("A45B0C0126", 13) == "109675097031")
    assert (convert_in_baza_10("A45B0C0126", 14) == "213123977702")
    assert (convert_in_baza_10("A45B0C0126", 15) == "395665357761")
    assert (convert_in_baza_10("01234567890ABCDEF", 16) == "1311768467294899695")

def test_convert_intermediar():
    pass