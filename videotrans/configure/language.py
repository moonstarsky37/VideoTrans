# -*- coding: utf-8 -*-
translate_language = {
    "zh": {
        "selectmp4": "选择mp4视频",
        "selectsavedir": "选择翻译后存储目录",
        "proxyerrortitle": "代理错误",
        "proxyerrorbody": "无法访问google服务，请正确设置代理",
        "softname": "视频字幕翻译和配音",
        "anerror": "出错了",
        "selectvideodir": "必须选择要翻译的视频",
        "sourenotequaltarget": "源语言和目标语言不得相同",
        "shoundselecttargetlanguage": "必须选择一个目标语言",
        "running": "执行中",
        "ing": "执行中",
        "exit": "退出",
        "end": "已结束(点击重新开始)",
        "stop": "已停止(点击开始)",
        "subtitleandvoice_role": "不能既不嵌入字幕又不选择配音角色，二者至少选一",
        "waitrole":"正在获取可用配音角色，请稍等重新选择",
        "downloadmodel":"模型不存在，请去下载后存放到:",
        "modelpathis":"当前模型路径是:",
        "modellost":"模型下载出错或者下载不完整，请重新下载后存放到 models目录下",
        "embedsubtitle":"硬字幕嵌入",
        "softsubtitle":"软字幕",
        "nosubtitle":"不添加字幕",
        "baikeymust":"你必须填写百度key",
        "chatgptkeymust":"你必须填写chatGPT key",
        "waitsubtitle":"等待编辑字幕(点击继续合成)",
        "waitforend":"正在合成视频",
        "createdirerror":"创建目录失败",
        "processingstatusbar":"正在处理视频:[{var1}],还有[{var2}]个在等待处理",
        "confirmstop":"确认停止执行?如果字幕生成一半，再次启动可能不完整，可以手动删掉tmp目录",
        "deepl_authkey":"你必须填写DeepL的授权key",
        "deepl_nosupport":"DeepL不支持翻译为该语言",
        "wait_edit_subtitle":"等待修改字幕",
        "autocomposing":"秒倒计时后将自动合成视频，修改字幕编辑区任意内容后将停止倒计时",
        "queding":"确定",
        "hechengchucuo":"合成出错，缺少文件:",
        "installffmpeg":"未找到 ffmpeg，软件不可用，请去 ffmpeg.org 下载并加入到系统环境变量",
        "yinsekelong":"音色克隆将使用  coqui.ai  所提供的 Api 服务，上传一段音频用于提取音色特征，然后用此特征作为配音角色，从而实现自定义的音色配音",
        "yinsekaifazhong":"音色克隆开发中",
        "whisper_type_all":"整体识别",
        "whisper_type_split":"预先分割",
        "waitclear":"正在关闭后台进程",
        "subtitle_tips":" 在此可编辑字幕信息，或拖动已有srt文件到此处松开 ",
        "setdeepl_authkey":"必须设置DeepL 授权token",
        "setdeeplx_address":"必须设置你的 DeepLX 地址和端口，比如 127.0.0.1:1188",
        "mustberole":"必须选择一个配音角色",
        "qingqueren":"请确认",
        "only_srt":"既未选择嵌入字幕也未选择配音角色，将仅创建字幕srt文件到目录文件夹，点Yes将继续执行，否则取消",
    },
    "en": {
        "qingqueren":"Please confirm",
        "only_srt":"Not select subtitle and not select dubbing role，will only create srt file，click Yes to continue,else cancel",
        "mustberole":"must be selet role for listen",
        "setdeepl_authkey":"must be set DeepL token",
        "setdeeplx_address":"must be set DeepLX address and port",
        "subtitle_tips":" Edit subtitle here or drap srt file to here ",
        "waitclear":"closing process",
        "whisper_type_all":"whole",
        "whisper_type_split":"first split",
        "processingstatusbar":"Process video:[{var1}] total, [{var2}] waitting",
        "yinsekelong": "Timbre cloning will use the API service provided by [coqui.ai], which can extract timbre features from a piece of audio. These features will then be used as the voice for dubbing characters, achieving custom dubbing with any desired timbre.",
        "yinsekaifazhong": "Timbre cloning is under development.",
        "installffmpeg":"ffmpeg not found, the software is not available. Please download it from ffmpeg.org and add it to the system's environment variables.",
        "hechengchucuo":"Composing video error，lost file:",
        "queding":"Confirm",
        "wait_edit_subtitle":"Wait for edit subtitle",
        "autocomposing":" seconds After the countdown, the video will be automatically synthesized. After modifying any content in the subtitle editing area, the countdown will stop",
        "deepl_nosupport":"DeepL don't support translation to the language",
        "deepl_authkey":"You need an DeepL authentication key",
        "confirmstop":"Stop this task?",
        "prcoessingstatusbar":"Processing video: [{var1}], with [{var2}] waiting to be processed",
        "createdirerror":"create dir error",
        "waitforend":"Composing video",
        "waitsubtitle":"Wait edit subtitle(click for continue)",
        "baikeymust":"input your baidu key",
        "chatgptkeymust":"input your chatgpt key",
        "nosubtitle":"No Subtitle",
        "embedsubtitle":"Embed subtitle",
        "softsubtitle":"Soft subtitle",
        "modellost":"There is an error in the model download or the download is incomplete. Please re-download and store it in the models directory.",
        "modelpathis":"Model storage path:",
        "downloadmodel":"Model does not exist, download it and save to:",
        "waitrole":"getting voice role list,hold on",
        "selectsavedir": "select an dir for output",
        "selectmp4": "select an mp4 video",
        "subtitleandvoice_role": "embedding subtitles or selecting voiceover characters must be set, meaning ‘neither embedding subtitles nor selecting voiceover characters’ is not allowed.",
        "proxyerrortitle": "Proxy Error",
        "shoundselecttargetlanguage": "Must select a target language ",
        "proxyerrorbody": "Failed to access Google services. Please set up the proxy correctly.",
        "softname": "Video Subtitle Translation and Dubbing",
        "anerror": "An error occurred",
        "selectvideodir": "You must select the video to be translated",
        "sourenotequaltarget": "Source language and target language must not be the same",
        "running": "Running",
        "ing": "Running",
        "exit": "Exit",
        "end": "Ended(click reststart)",
        "stop": "Stop(click start)"
    }
}


#  名称: google翻译代码and语音识别代码，字幕语言代码，百度翻译代码，deep代码
language_code_list={
    "zh":{
        "中文简": ['zh-cn', 'chi','zh','ZH'],
        "中文繁": ['zh-tw', 'chi','cht','ZH'],
        "英语": ['en', 'eng','en','EN-US'],
        "法语": ['fr', 'fre','fra','FR'],
        "德语": ['de', 'ger','de','DE'],
        "日语": ['ja', 'jpn','jp','JA'],
        "韩语": ['ko', 'kor','kor','KO'],
        "俄语": ['ru', 'rus','ru','RU'],
        "西班牙语": ['es', 'spa','spa','ES'],
        "泰国语": ['th', 'tha','th','No'],
        "意大利语": ['it', 'ita','it','IT'],
        "葡萄牙语": ['pt', 'por','pt','PT'],
        "越南语": ['vi', 'vie','vie','No'],
        "阿拉伯语": ['ar', 'are','ara','No']
    },
    "en":{
        "Simplified_Chinese": ['zh-cn', 'chi','zh','ZH'],
        "Traditional_Chinese": ['zh-tw', 'chi','cht','ZH'],
        "English": ['en', 'eng','en','EN-US'],
        "French": ['fr', 'fre','fra','FR'],
        "German": ['de', 'ger','de','DE'],
        "Japanese": ['ja', 'jpn','jp','JA'],
        "Korean": ['ko', 'kor','kor','KO'],
        "Russian": ['ru', 'rus','ru','RU'],
        "Spanish": ['es', 'spa','spa','ES'],
        "Thai": ['th', 'tha','th','No'],
        "Italian": ['it', 'ita','it','IT'],
        "Portuguese": ['pt', 'por','pt','PT'],
        "Vietnamese": ['vi', 'vie','vie','No'],
        "Arabic": ['ar', 'are','ara','No']
    }
}

# cli language ccode
clilanglist = {
    "zh-cn": ['zh-cn', 'chi'],
    "zh-tw": ['zh-tw', 'chi'],
    "en": ['en', 'eng'],
    "fr": ['fr', 'fre'],
    "de": ['de', 'ger'],
    "ja": ['ja', 'jpn'],
    "ko": ['ko', 'kor'],
    "ru": ['ru', 'rus'],
    "es": ['es', 'spa'],
    "th": ['th', 'tha'],
    "it": ['it', 'ita'],
    "pt": ['pt', 'por'],
    "vi": ['vi', 'vie'],
    "ar": ['ar', 'are']
}
english_code_bygpt=list(language_code_list['en'].keys())
