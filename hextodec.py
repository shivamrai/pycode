def hextodecimal(array :list):
    convertedArray = []
    for item in array:
        convertedArray.append(int(item),10)
    return convertedArray

if __name__ == "__main__":
    toBeConvertedA = ['377A','BCAF',	'271C0003',	'0241DD5F',	'17000000',	'00000000',	'58000000',	'00000000',	'BAF0646A',	
    '00221BC9','C273209C',	'AA0F0A55',	'3F195B82',	'2E8172D5',	'83000001',	'04060001',	'09170007',	'0B010001',	'23030101']
    toBeConvertedB = ['055D0000',	'01000C11',	'00080A01',	'D1DA43C2',	'00000501',	'111B0064',	'006F006E',	'00740066',	'00750063',
    '006B0069',	'00740075',	'00700000',	'00140A01',	'0080F1F4',	'CEAC5ED1',	'01150601',	'00208080',	'81000000']
    print('set1')
    print(hextodecimal(toBeConvertedA))
    print('set2')
    print(hextodecimal(toBeConvertedB))