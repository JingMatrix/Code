export const FILE_TYPE_VIDEO = "filetype_video";
export const FILE_TYPE_AUDIO = "filetype_audio";
export const FILE_TYPE_PPT = "filetype_ppt";
export const FILE_TYPE_XLS = "filetype_xls";
export const FILE_TYPE_DOC = "filetype_doc";
export const FILE_TYPE_PDF = "filetype_pdf";
export const FILE_TYPE_ZIP = "filetype_zip";
export const FILE_TYPE_IMG = "filetype_img";
export const FILE_TYPE_OTHERS = "filetype_others";
export const FILE_TYPE_UNKNOWN = "filetype_unknown";
export const FILE_TYPE_FOLDER = "filetype_folder";

export const PROJECT_NAME = "大力盘搜索";
export const DOMAIN = "https://www.dalipan.com";
export const TITLE = `网盘搜索，就用${PROJECT_NAME} - 最好用的百度网盘搜索引擎，${DOMAIN}。`;
export const KEYWORDS = `${PROJECT_NAME},盘搜搜,大力盘,大力盘搜索,大力搜索盘,网盘搜索,电影下载,迅雷下载,bt下载,种子下载,电子书下载,百度云盘搜索,网盘搜索引擎,百度网盘搜索`;
export const DESCRIPTION = `${PROJECT_NAME}支持百度云搜索，可快速搜索百度网盘资源中的有效连接，自动识别无效的百度云网盘资源，每天更新海量资源。`;

export const RESOURCE_FROM = {
  sopan_spider: {
    name: "52搜盘",
    url: "http://www.52sopan.com",
  },
  panduoduo: {
    name: "盘多多",
    url: "http://www.panduoduo.net",
  },
  "56wangpan": {
    name: "56网盘",
    url: "http://www.56wanpan.com",
  },
  pansoso: {
    name: "盘搜搜",
    url: "http://www.pansoso.com",
  },
  xiaobaipan: {
    name: "小白盘",
    url: "http://xiaobaipan.com",
  },
  quzhuanpan: {
    name: "去转盘",
    url: "https://www.quzhuanpan.com",
  },
};

export const FILTER = {
  type: {
    7: {
      name: "BT种子",
      value: 7,
    },
    6: {
      name: "压缩包",
      value: 6,
    },
    5: {
      name: "软件",
      value: 5,
    },
    4: {
      name: "文档",
      value: 4,
    },
    3: {
      name: "图片",
      value: 3,
    },
    2: {
      name: "音乐",
      value: 2,
    },
    1: {
      name: "视频",
      value: 1,
    },
    0: {
      name: "文件夹",
      value: 0,
    },
  },
  time: {
    3: {
      name: "最近一年",
      value: 365,
    },
    2: {
      name: "最近半年",
      value: 180,
    },
    1: {
      name: "最近一月",
      value: 30,
    },
    0: {
      name: "最近一周",
      value: 7,
    },
  },
  size: {
    3: {
      name: "大于2GB",
      minSize: 2147483648,
    },
    2: {
      name: "200MB-2GB",
      maxSize: 2147483648,
      minSize: 209715200,
    },
    1: {
      name: "20MB-200MB",
      maxSize: 209715200,
      minSize: 20971520,
    },
    0: {
      name: "小于20MB",
      maxSize: 20971520,
    },
  },
  searchtype: {
    1: {
      name: "模糊搜索",
      value: "match",
    },
    0: {
      name: "精确搜索",
      value: "precise",
    },
  },
};

export const LINKS = [
  {
    text: "北邮人导航",
    link: "http://byr.wiki?from=dalipan",
  },
  {
    text: "柴杜导航",
    link: "https://www.chaidu.com?from=dalipan",
  },
  {
    text: "24K导航",
    link: "https://www.24kdh.com?from=dalipan",
  },
  {
    text: "爱达杂货铺",
    link: "https://adzhp.cn?from=dalipan",
  },
  {
    text: "龙喵网",
    link: "https://ailongmiao.com/?from=dalipan",
  },
  {
    text: "效率集",
    link: "http://www.xiaolvji.com/?from=dalipan",
  },
  {
    text: "文叔叔传文件",
    link: "https://www.wenshushu.cn/?from=dalipan",
  },
  {
    text: "破解软件集",
    link: "http://www.dayouzi.net/?from=dalipan",
  },
  {
    text: "飞飞盘",
    link: "http://www.feifeipan.com/?from=dalipan",
  },
  {
    text: "果汁导航",
    link: "http://guozhivip.com/?from=dalipan",
  },
  {
    text: "河小兔导航",
    link: "http://www.hexiaotu.com/?from=dalipan",
  },
  {
    text: "超能搜",
    link: "https://www.chaonengsou.com/?from=dalipan",
  },
  {
    text: "万网搜",
    link: "https://www.wanwangsou.com/?from=dalipan",
  },
  {
    text: "毕方铺",
    link: "https://www.iizhi.cn/?from=dalipan",
  },
];

export const HOTWORDS = [
  "课程",
  "资料",
  "会计",
  "考研",
  "学习",
  "书单",
  "考试",
  "英语",
  "小说",
  "漫画",
  "电影",
  "游戏",
  "电子书",
  "美女",
  "Python",
  "JavaScript",
  "C语言",
  "人工智能",
  "深度学习",
  "数据分析",
  "PS视频教程",
  "PPT模版",
  "设计素材",
  "王者荣耀",
  "阴阳师",
  "炉石传说",
  "史记",
  "红楼梦",
  "教育短片",
];

export const WAYS = [
  "免费-普通线路1",
  "飞侠赞助-电信专线2",
  "摆渡赞助-混合专线3",
  "紫玉赞助-混合高速4",
];
