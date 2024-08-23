from typing import List, Optional

class Image:
    def __init__(self, url: str):
        self.url = url

class UserFollowInfo:
    def __init__(self, following_count: int, follower_count: int, follow_status: int, push_status: int):
        self.following_count = following_count
        self.follower_count = follower_count
        self.follow_status = follow_status
        self.push_status = push_status

class ExtendedUser:
    def __init__(self, id: int, nickname: str, bio_description: str, avatar_thumb: Image, 
                 avatar_medium: Image, avatar_large: Image, follow_info: UserFollowInfo, 
                 sec_uid: str, gifter_level: int, team_member_level: int, 
                 is_moderator: bool, is_new_gifter: bool, is_subscriber: bool, top_gifter_rank: Optional[int]):
        self.id = id
        self.nickname = nickname
        self.bio_description = bio_description
        self.avatar_thumb = avatar_thumb
        self.avatar_medium = avatar_medium
        self.avatar_large = avatar_large
        self.follow_info = follow_info
        self.sec_uid = sec_uid
        self.gifter_level = gifter_level
        self.team_member_level = team_member_level
        self.is_moderator = is_moderator
        self.is_new_gifter = is_new_gifter
        self.is_subscriber = is_subscriber
        self.top_gifter_rank = top_gifter_rank

class ExtendedGiftStruct:
    def __init__(self, id: int, repeat_count: int, repeat_end: bool, type: int, diamond_count: int, 
                 name: str, icon: Image, describe: str):
        self.id = id
        self.repeat_count = repeat_count
        self.repeat_end = repeat_end
        self.type = type
        self.diamond_count = diamond_count
        self.name = name
        self.icon = icon
        self.describe = describe

class GiftEvent:
    def __init__(self, to_user: ExtendedUser, user: ExtendedUser, gift: ExtendedGiftStruct):
        self.to_user = to_user
        self.user = user
        self.gift = gift

    @property
    def streaking(self) -> bool:
        return not bool(self.gift.repeat_end)


def convert_to_gift_event(data):
    def create_image(url: str) -> Image:
        return Image(url)

    def create_user(data) -> ExtendedUser:
        avatar_thumb = create_image(data['profilePictureUrl'])
        avatar_medium = create_image(data['userDetails']['profilePictureUrls'][0])
        avatar_large = create_image(data['userDetails']['profilePictureUrls'][0])
        follow_info = UserFollowInfo(
            following_count=data['followInfo']['followingCount'],
            follower_count=data['followInfo']['followerCount'],
            follow_status=data['followInfo']['followStatus'],
            push_status=data['followInfo']['pushStatus']
        )
        return ExtendedUser(
            id=int(data['userId']),
            nickname=data['nickname'],
            bio_description=data['userDetails']['bioDescription'],
            avatar_thumb=avatar_thumb,
            avatar_medium=avatar_medium,
            avatar_large=avatar_large,
            follow_info=follow_info,
            sec_uid=data['secUid'],
            gifter_level=data['gifterLevel'],
            team_member_level=data['teamMemberLevel'],
            is_moderator=data['isModerator'],
            is_new_gifter=data['isNewGifter'],
            is_subscriber=data['isSubscriber'],
            top_gifter_rank=data['topGifterRank']
        )

    def create_gift(data) -> ExtendedGiftStruct:
        icon = create_image(data['giftPictureUrl'])
        return ExtendedGiftStruct(
            id=int(data['giftId']),
            repeat_count=int(data['repeatCount']),
            repeat_end=data['repeatEnd'],
            type=int(data['giftType']),
            diamond_count=int(data['diamondCount']),
            name=data['giftName'],
            icon=icon,
            describe=data['describe']
        )

    to_user = create_user(data['data'])
    user = create_user(data['data'])
    gift = create_gift(data['data'])

    return GiftEvent(to_user=to_user, user=user, gift=gift)


# Example usage:
gift_event_data = {
    "event": "gift",
    "data": {
        "giftId": 11606,
        "repeatCount": 1,
        "groupId": "1723466642623",
        "userId": "6552476891844214786",
        "secUid": "MS4wLjABAAAAJwQhdP3wnmL_j_F7q84bSGqkjl9Sq3An-E4tZgeVEP37Yx_-eMHVUGY3NmDTLTd2",
        "uniqueId": "2166909757",
        "nickname": "Ma Kết",
        "profilePictureUrl": "https://p16-sign-sg.tiktokcdn.com/aweme/100x100/tos-alisg-avt-0068/97d8c69ed3d89ca873bc38a39646df09.webp?lk3s=a5d48078&nonce=66040&refresh_token=71fc28d8b4f872f3ae58be5fb9e15c09&x-expires=1723636800&x-signature=pyvWwVjhTj3E8CppC76ofv7CR1c%3D&shp=a5d48078&shcp=fdd36af4",
        "followRole": 0,
        "userBadges": [],
        "userSceneTypes": [],
        "userDetails": {
            "createTime": "0",
            "bioDescription": "",
            "profilePictureUrls": [
                "https://p16-sign-sg.tiktokcdn.com/aweme/100x100/tos-alisg-avt-0068/97d8c69ed3d89ca873bc38a39646df09.webp?lk3s=a5d48078&nonce=66040&refresh_token=71fc28d8b4f872f3ae58be5fb9e15c09&x-expires=1723636800&x-signature=pyvWwVjhTj3E8CppC76ofv7CR1c%3D&shp=a5d48078&shcp=fdd36af4"
            ]
        },
        "followInfo": {
            "followingCount": 1469,
            "followerCount": 45,
            "followStatus": 0,
            "pushStatus": 0
        },
        "isModerator": False,
        "isNewGifter": False,
        "isSubscriber": False,
        "topGifterRank": None,
        "gifterLevel": 15,
        "teamMemberLevel": 8,
        "msgId": "7402232527261911816",
        "createTime": "1723466642925",
        "displayType": "webcast_aweme_gift_send_message",
        "label": "{0:user} sent {1:gift} {2:string}",
        "repeatEnd": False,
        "gift": {
            "gift_id": 11606,
            "repeat_count": 1,
            "repeat_end": 0,
            "gift_type": 1
        },
        "describe": "đã gửi Thắp sáng trái tim",
        "giftType": 1,
        "diamondCount": 10,
        "giftName": "Thắp sáng trái tim",
        "giftPictureUrl": "https://p19-webcast.tiktokcdn.com/img/maliva/webcast-va/resource/fcf1ea7d8ca69927eb524b45edeeec1e.png~tplv-obj.png",
        "timestamp": 1723466642926,
        "receiverUserId": "7385200487454360584",
        "originalName": "Light Your Heart",
        "originalDescribe": "Sent Light Your Heart"
    }
}

gift_event = convert_to_gift_event(gift_event_data)
print(gift_event)
