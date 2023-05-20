Men = {"Jake" : ["Lizzy", "Alissa", "Sarah", "Lexi"],
     "Max" : ["Lizzy", "Sarah", "Lexi", "Alissa"],
     "Abdu": ["Lizzy", "Alissa", "Lexi", "Sarah"],
     "Leo" : ["Lexi", "Lizzy", "Alissa", "Sarah"]}

Women = {"Lizzy" : ["Max", "Jake", "Abdu", "Leo"], 
         "Alissa": ["Abdu", "Leo", "Max", "Jake"],
         "Sarah" : ["Jake", "Abdu", "Max", "Leo"], 
         "Lexi"  : ["Leo", "Jake", "Abdu", "Max"]}

def stableMatching_GS(M: dict(), W: dict()):
    finalCouples = {}
    possibleProposals = { man : woman for man, woman in M.items() }
    #print(possibleProposals)
    freeMen = [man for man in M.keys()]
    while(freeMen):
        man = freeMen[0]
        print(f"Dealing with {man}...")
        for woman in M[man]:
            print(f"Proposing to {woman}")
            if woman not in finalCouples:
                print(f"{woman} is free and now she's engaged to {man} \n")
                finalCouples.update({woman : man})
                freeMen.pop(0)
                break
            else:
                print(f"{woman} is already taken...")
                currentPartnerRanking = W[woman].index(finalCouples[woman])
                potentialPartnerRanking = W[woman].index(man)
                if (currentPartnerRanking > potentialPartnerRanking): 
                    print(f"but she's not happy with {finalCouples[woman]}")
                    print(f"Now {woman} is engaged to {man}! \n")
                    freeMen.pop(0)
                    freeMen.append(finalCouples[woman])
                    finalCouples.update({woman : man})
                    break
                else:
                    continue

    finalCouples = {man : woman for woman, man in finalCouples.items()}
    return finalCouples
                
if __name__ == "__main__":
    print(f"Stable Matchings: {stableMatching_GS(Men, Women)}")