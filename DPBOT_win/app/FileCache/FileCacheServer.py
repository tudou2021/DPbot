from OutPut.outPut import op
import os


def returnCachePath():
    """
    返回缓存文件夹路径
    :return:
    """
    # 获取当前文件的绝对路径
    current_file = os.path.abspath(__file__)
    # 获取当前文件所在目录
    current_dir = os.path.dirname(current_file)
    # 获取项目根目录（向上一级）
    project_root = os.path.dirname(current_dir)
    # 返回FileCache目录的路径
    fileCachePath = os.path.join(project_root, 'FileCache')
    return fileCachePath


def returnPicCacheFolder():
    """
    返回图片缓存文件夹
    :return:
    """
    return os.path.join(returnCachePath(), 'picCacheFolder')


def returnVideoCacheFolder():
    """
    返回视频缓存文件夹
    :return:
    """
    return os.path.join(returnCachePath(), 'videoCacheFolder')


def returnFishCacheFolder():
    """
    返回摸鱼日历缓存文件夹
    :return:
    """
    return os.path.join(returnCachePath(), 'FishCacheFolder')


def returnGaoDeCacheFolder():
    """
    返回高德地图缓存文件夹
    :return:
    """
    return os.path.join(returnCachePath(), 'gaodeCacheFolder')


def returnAiPicFolder():
    """
    返回Ai生成图像缓存文件夹
    :return:
    """
    return os.path.join(returnCachePath(), 'aiPicCacheFolder')


def returnAvatarFolder():
    """
    返回微信头像缓存文件夹
    :return:
    """
    return os.path.join(returnCachePath(), 'weChatAvatarFolder')


def returnGameFolder():
    """
    返回游戏缓存文件夹
    :return:
    """
    return os.path.join(returnCachePath(), 'gameCacheFolder')

def returnAudioFolder():
    """
    返回语音缓存文件夹
    :return:
    """
    return os.path.join(returnCachePath(), 'audioCacheFolder')

def returnWebServerFolder():
    """
    返回WebServer服务缓存文件夹
    :return:
    """
    return os.path.join(returnCachePath(), 'webServerCacheFolder')

def clearCacheFolder():
    """
    清空缓存文件夹所有文件
    :return:
    """
    if os.path.exists(returnAiPicFolder()):
        file_lists = []
        file_lists += [os.path.join(returnPicCacheFolder(), file) for file in os.listdir(returnPicCacheFolder())]
        file_lists += [os.path.join(returnVideoCacheFolder(), file) for file in os.listdir(returnVideoCacheFolder())]
        file_lists += [os.path.join(returnFishCacheFolder(), file) for file in os.listdir(returnFishCacheFolder())]
        file_lists += [os.path.join(returnGaoDeCacheFolder(), file) for file in os.listdir(returnGaoDeCacheFolder())]
        file_lists += [os.path.join(returnAiPicFolder(), file) for file in os.listdir(returnAiPicFolder())]
        file_lists += [os.path.join(returnAvatarFolder(), file) for file in os.listdir(returnAvatarFolder())]
        file_lists += [os.path.join(returnGameFolder(), file) for file in os.listdir(returnGameFolder())]
        file_lists += [os.path.join(returnAudioFolder(), file) for file in os.listdir(returnAudioFolder())]
        file_lists += [os.path.join(returnWebServerFolder(), file) for file in os.listdir(returnWebServerFolder())]
        for rm_file in file_lists:
            os.remove(rm_file)
        return True
    else:
        initCacheFolder()
        clearCacheFolder()


def initCacheFolder():
    """
    初始化缓存文件夹
    :return:
    """
    if not os.path.exists(returnPicCacheFolder()):
        os.mkdir(returnPicCacheFolder())
    if not os.path.exists(returnVideoCacheFolder()):
        os.mkdir(returnVideoCacheFolder())
    if not os.path.exists(returnFishCacheFolder()):
        os.mkdir(returnFishCacheFolder())
    if not os.path.exists(returnGaoDeCacheFolder()):
        os.mkdir(returnGaoDeCacheFolder())
    if not os.path.exists(returnAiPicFolder()):
        os.mkdir(returnAiPicFolder())
    if not os.path.exists(returnAvatarFolder()):
        os.mkdir(returnAvatarFolder())
    if not os.path.exists(returnGameFolder()):
        os.mkdir(returnGameFolder())
    if not os.path.exists(returnAudioFolder()):
        os.mkdir(returnAudioFolder())
    if not os.path.exists(returnWebServerFolder()):
        os.mkdir(returnWebServerFolder())
    op(f'[+]: 初始化缓存文件夹成功!!!')


if __name__ == '__main__':
    initCacheFolder()
    # print(returnCachePath())
    clearCacheFolder()
