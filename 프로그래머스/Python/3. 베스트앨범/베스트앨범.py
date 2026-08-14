from collections import defaultdict

def solution(genres, plays):
    N = len(genres)
    
    dict = {}
    for i in range(N):
        genre = genres[i]
        play = plays[i]
        
        if genre in dict:
            dict[genre].append((play, i))
        else:
            dict[genre] = [(play, i)]
    
    # 어떤 장르가 노래 많은지
    # 장르 내에서 어떤 노래가 많은지
    genre_len = []
    for genre in dict:
        genre_len.append((genre, sum(x[0] for x in dict[genre])))
        dict[genre].sort(key = lambda x: (-x[0], x[1]))
    
    genre_len.sort(key = lambda x: (-x[1]))
    
    # print(dict)
    # print(genre_len)
    
    best = []
    for g, _ in genre_len:
        if len(dict[g]) == 1:
            best.append(dict[g][0][1])
        else:
            best.append(dict[g][0][1])
            best.append(dict[g][1][1])
        # print('added')
        # print(best)
                         
                         
    return best