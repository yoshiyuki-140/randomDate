

# まず作るべきものは、施設を選択できるようにする。
# ランダムで施設を選択できるようにする。


museums = [
    {  
        "facility_name": "中村記念美術館",
        "business_hour": "10:00 - 16:30",
        "last_admission_time": "16:00"
    },
    {
        "facility_name": "金沢能楽美術館",
        "business_hour": "10:00 - 18:00",
        "last_admission_time": "17:30"
    },
    {
        "facility_name": "金箔工芸館",
        "business_hour": "09:30 - 17:00",
        "last_admission_time": "16:30"
    },
    {
        "facility_name": "２１世紀美術館（展覧会ゾーン）",
        "business_hour": "10:00 - 18:00（金・土は20:00まで）",
        "last_admission_time": ""
    },
    {
        "facility_name": "２１世紀美術館（交流ゾーン）",
        "business_hour": "09:00 - 22:00",
        "last_admission_time": ""
    },
    {
        "facility_name": "いしかわ生活工芸ミュージアム",
        "business_hour": "09:00 - 17:00",
        "last_admission_time": "16:45"
    },
    {
        "facility_name": "国立工芸館",
        "business_hour": "09:30 - 17:30",
        "last_admission_time": "17:00"
    }
]

facility_names = [museum["facility_name"] for museum in museums ]

business_hours = [museum["business_hour"] for museum in museums]

last_admission_time = [museum["last_admission_time"] for museum in museums]


if __name__ == "__main__":
    print(facility_names)
    print(business_hours)
    print(last_admission_time)

# 配列からランダムで要素を選択する

import random

facility_name = random.choice(facility_names)
print(facility_name)
