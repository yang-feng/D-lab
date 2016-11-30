#分析電影
#資料來源：IMDB電影資料集(https://www.kaggle.com/deepmatrix/imdb-5000-movie-dataset)
#D-LAB Python X 使用者體驗設計 basic4 作業
#輸入CSV檔名為：movie_metadata
#輸出排序票房前五名的資料
#學生：Feng jun yang (young)  教師：Mars
#2016年12月1日


#自訂排序函式
def my_sort(mov_dic):
    return mov_dic['gross']

#List to dic function
def list_to_dict(Li):
    dct = {}
    column_name=['color','director_name','num_critic_for_reviews','duration','director_facebook_likes','actor_3_facebook_likes','actor_2_name','actor_1_facebook_likes','gross','genres','actor_1_name','movie_title','num_voted_users','cast_total_facebook_likes','actor_3_name','facenumber_in_poster','plot_keywords','movie_imdb_link','num_user_for_reviews','language','country','content_rating','budget','title_year','actor_2_facebook_likes','imdb_score','aspect_ratio','movie_facebook_likes']
    for i in range(28):
        dct[column_name[i]] = Li[i]        
    return dct  


#變數定義
mov_data_set = []
mov_dic = {}

	
#開啟CSV檔
file = open("movie_metadata.csv",mode='r',encoding='utf-8')
file.seek(0)
log_file = open("mov_data_log.txt",'w',encoding='utf-8')

#一次處理一行，以逗號切割，並塞到字典中
#電影中的逗號需另外處理
for line in file:
    line = line.strip()
    if '\"' in line:
        split_data = line.split(',')
        split_data[11] = split_data[11] + "," + split_data[12]
        del split_data[12]
    
        
    else:
        split_data = line.split(',')
    
    mov_data_set.append(list_to_dict(split_data))

	#刪除第一行標題欄位
del mov_data_set[0]

for Ranking in range(5+1):
    mov_dic = sorted(mov_data_set,key=my_sort,reverse=True)[Ranking]
    print(u'第'+str(Ranking+1) + u'名  票房：'  +  mov_dic['gross'])
    print(u'電影名稱：' + mov_dic['movie_title'] )
    print(u'類型：' + mov_dic['genres'])
    print(u'評分：' + mov_dic['imdb_score'] + u'成本：' + mov_dic['budget'])
    print(u'演員一：' + mov_dic['actor_1_name']+ "  " + mov_dic['actor_1_facebook_likes'] +"個讚")
    print(u'演員二：' + mov_dic['actor_2_name']+ "  " + mov_dic['actor_2_facebook_likes'] +"個讚")
    print(u'演員三：' + mov_dic['actor_3_name']+ "  " + mov_dic['actor_3_facebook_likes'] +"個讚")
    print(u'導演：' + mov_dic['director_name']+ "  " + mov_dic['director_facebook_likes'] +"個讚")


#將全部紀錄寫入log_file檔中
#log_file.write(str(sorted(mov_data_set,key=my_sort,reverse=True)[0]))

#將檔案關閉
file.close
log_file.close