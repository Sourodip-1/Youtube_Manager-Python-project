import json

def load_data():
    try:
        with open("youtube.txt","r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    with open("youtube.txt","w") as file:
        json.dump(videos,file)

def list_all_videos(videos):
    for index,video in enumerate(videos,start=1):
        print()
        print('*'*70)
        print(f"{index}. {video['name']} Duration: {video['time']}") #imp to understand
def add_video(videos):
    name=input("enter video name: ")
    time=input("enter video time: ")
    videos.append({'name':name,"time": time})
    save_data_helper(videos)


def update_video(videos):
    list_all_videos(videos)
    index= int(input("enter the video number to update: "))
    if 1<= index <=len(videos):
        name=input("enter new video name: ")
        time=input("eneter video time: ")
        videos[index-1]={'name':name,"time":time}
        save_data_helper(videos)
    else:
        print("invalid input")

def delete_video(videos):
    list_all_videos(videos)
    index= int(input("enter the video number to delete: "))
    if index in range(1,len(videos)):
        print(f"{videos.pop(index-1)} was removed from the array")
        save_data_helper(videos)
    else:
         print("invalid input")   
                         
def main():
    videos=load_data()
    while True:
        print("\n Youtube Manager | Choose An Option")
        print("1. List all youtube Videos")
        print("2. Add a Youtube Video")
        print("3. Update a Youtube Video Details")
        print("4. Delete a Youtube Video")
        print("5. Exit The App")
        choice=input("Enter Your Choice: ")
        # print(videos)

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _ :
                print("invalid Choice") 

if __name__ == "__main__":
    main()