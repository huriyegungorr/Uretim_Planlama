def uretimPlanlama(n, m, isSureleri, gecisMaliyetleri):
    dp = [[float('inf')] * m for _ in range(n)]

    # n*m kadar uzay karmaşıklığı O(n*m) n tane iş m tane makine var 
    for j in range(m):
        dp[0][j] = isSureleri[0][j]

    # iç içe for döngüleri n*m*m kere çalıştığından O(n*m^2)
    #tüm işleri şimdi kullanılan makineler ve eski makineleri gezerek önceki ve şimdiki süreleri ve geçiş maaliyetlerini toplar ve en kısa türeyi buradan çeker
    for i in range(1, n):
        for j in range(m):
            for k in range(m):
                dp[i][j] = min(dp[i][j], dp[i-1][k] + gecisMaliyetleri[k][j] + isSureleri[i][j])

    # Son iş için en küçük süreyi döndür
    return min(dp[-1])


isSureleri = [
    [2, 10],
    [8, 16],
    [4, 6]
]

gecisMaliyetleri = [
    [1, 2],
    [5, 2]
]

n = 3  # iş sayısı
m = 2  # makine sayısı

print("en kisa sure:" , uretimPlanlama(n, m, isSureleri, gecisMaliyetleri))
