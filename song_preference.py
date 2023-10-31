import numpy as np
 
# Define a function that takes two lists as input, sorts the first list based on
# the order of the second list, and returns the sorted list as a numpy array
def sort_list(list1, list2):
    # Use numpy's argsort function to get the indices that would sort the second list
    idx = np.argsort(list2)
    # Index the first list using the sorted indices and return the result as a numpy array
    return np.array(list1)[idx]
def songer(pref):
    n_songs = len(pref[0])
    n_users = len(pref)
    song_pref = [0]*n_songs
    for i in range(n_songs):
        for j in range(i+1,n_songs):
            count = 0
            for k in range(n_users):
                if pref[k].index(i) < pref[k].index(j):
                    count += 1
            if count > n_users//2:
                song_pref[i] -= 1
            elif count < n_users//2:
                song_pref[j] -= 1
            else:
                song_pref[i] -= 1
                song_pref[j] -= 1
    ranking = [0]*n_songs
    # ranking on basis of song_pref
    print(song_pref)
    idx=np.argsort(song_pref)
    ranking=np.array(list(range(n_songs)))[idx]

    return ranking


pref=[[0, 1, 3, 2], [0, 2, 3, 1], [1, 0, 3, 2], [2, 1, 0, 3], [0, 3, 1, 2]]

# pref=[[0,1,2,3],[1,2,3,0],[2,3,0,1],[3,0,1,2]]
print(songer(pref))