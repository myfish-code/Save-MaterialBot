n = int(input())
l = []
for q in range(0,n):
    l1 = list(map(str,input().split()))
    for w in range(0,len(l1)):
        l.append(l1[w])
j = []
for a in range(0,len(l)):
    k = list(l[a])
    j.append(k)

for g in range(0,len(j)):
    for f in range(0,len(l[g])):

        if j[g][f] == "à":
            j[g].insert(f, "а")

            del j[g][f+1]
        if j[g][f] == "á":
            j[g].insert(f, "б")

            del j[g][f+1]
        if j[g][f] == "â":
            j[g].insert(f, "в")

            del j[g][f+1]
        if j[g][f] == "ã":
            j[g].insert(f, "г")

            del j[g][f+1]
        if j[g][f] == "ä":
            j[g].insert(f, "д")

            del j[g][f+1]
        if j[g][f] == "å":
            j[g].insert(f, "е")

            del j[g][f+1]
        if j[g][f] == "¼":
            j[g].insert(f, "е")

            del j[g][f+1]
        if j[g][f] == "æ":
            j[g].insert(f, "ж")

            del j[g][f+1]
        if j[g][f] == "ç":
            j[g].insert(f, "з")

            del j[g][f+1]
        if j[g][f] == "è":
            j[g].insert(f, "и")

            del j[g][f+1]
        if j[g][f] == "é":
            j[g].insert(f, "й")

            del j[g][f+1]
        if j[g][f] == "ê":
            j[g].insert(f, "к")

            del j[g][f+1]
        if j[g][f] == "ë":
            j[g].insert(f, "л")

            del j[g][f+1]
        if j[g][f] == "ì":
            j[g].insert(f, "м")

            del j[g][f+1]
        if j[g][f] == "í":
            j[g].insert(f, "н")

            del j[g][f+1]
        if j[g][f] == "î":
            j[g].insert(f, "о")

            del j[g][f+1]
        if j[g][f] == "ï":
            j[g].insert(f, "п")

            del j[g][f+1]
        if j[g][f] == "ð":
            j[g].insert(f, "р")

            del j[g][f+1]
        if j[g][f] == "ñ":
            j[g].insert(f, "с")

            del j[g][f+1]
        if j[g][f] == "ò":
            j[g].insert(f, "т")

            del j[g][f+1]
        if j[g][f] == "ó":
            j[g].insert(f, "у")

            del j[g][f+1]
        if j[g][f] == "ô":
            j[g].insert(f, "ф")

            del j[g][f+1]
        if j[g][f] == "õ":
            j[g].insert(f, "х")

            del j[g][f+1]
        if j[g][f] == "ö":
            j[g].insert(f, "ц")

            del j[g][f+1]
        if j[g][f] == "÷":
            j[g].insert(f, "ч")

            del j[g][f+1]
        if j[g][f] == "ø":
            j[g].insert(f, "ш")

            del j[g][f+1]
        if j[g][f] == "ù":
            j[g].insert(f, "щ")

            del j[g][f+1]
        if j[g][f] == "û":
            j[g].insert(f, "ы")

            del j[g][f+1]
        if j[g][f] == "ü":
            j[g].insert(f, "ь")

            del j[g][f+1]
        if j[g][f] == "ý":
            j[g].insert(f, "э")

            del j[g][f+1]
        if j[g][f] == "þ":
            j[g].insert(f, "ю")

            del j[g][f+1]
        if j[g][f] == "ÿ":
            j[g].insert(f, "я")

            del j[g][f+1]

        if j[g][f] == "✲":
            j[g].insert(f, "")

            del j[g][f+1]

        if j[g][f] == "✭":
            j[g].insert(f, "")

            del j[g][f+1]

        if j[g][f] == "✱":
            j[g].insert(f, "")

            del j[g][f+1]

        if j[g][f] == "✳":
            j[g].insert(f, "")

            del j[g][f+1]

        if j[g][f] == "✮":
            j[g].insert(f, "")

            del j[g][f+1]

    del[g][0]


for t in range(0,len(j)):
    for i in range(0,len(j[t])):
        print(j[t][i],end = "")
    print(end = " ")