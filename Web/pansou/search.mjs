import { request } from "./base.mjs";
import { FILTER, HOTWORDS, LINKS } from "./constants.mjs";

// put your token here
const token = "";
const localStorage = {
  getItem: () => {
    return token;
  },
};

export const getSearchResult = async ({
  keyword,
  page,
  size,
  ip,
  type,
  time,
  searchtype,
  line = 0,
}) => {
  if (keyword == null || keyword == undefined) {
    return null;
  }
  const params = {
    kw: keyword,
    page: page || 1,
    line,
    ip,
    site: "dalipan",
  };

  if (FILTER.type[type]) {
    params.category = FILTER.type[type].value;
  }
  if (FILTER.time[time]) {
    params.diffDay = FILTER.time[time].value;
  }
  if (FILTER.searchtype[searchtype]) {
    params.searchType = FILTER.searchtype[searchtype].value;
  }
  if (FILTER.size[size]) {
    if (FILTER.size[size].minSize) {
      params.minSize = FILTER.size[size].minSize;
    } else {
      params.minSize = 1;
    }
    if (FILTER.size[size].maxSize) {
      params.maxSize = FILTER.size[size].maxSize;
    } else {
      params.maxSize = 1099511627776;
    }
  }

  const data = await request({
    url: "/api/v1/pan/search",
    params,
    headers: {
      "X-Authorization": process.server ? "" : localStorage.getItem("token"),
    },
  });
  return data;
};

export const getRandomResources = async ({ ip, size = 10 }) => {
  return await request({
    url: "/api/v1/pan/query",
    params: {
      type: "random",
      size,
      ip,
    },
  });
};

export const getNewResources = async ({ ip, size = 10 }) => {
  return await request({
    url: "/api/v1/pan/query",
    params: {
      type: "new",
      size,
      ip,
    },
  });
};

export const getHotResources = async ({ ip, size = 10 }) => {
  return await request({
    url: "/api/v1/pan/query",
    params: {
      type: "views",
      size,
      ip,
    },
  });
};

export const getDownloadMostResources = async ({ ip, size = 10 }) => {
  return await request({
    url: "/api/v1/pan/query",
    params: {
      type: "download",
      size,
      ip,
    },
  });
};

export const getRecommendResources = async ({ ip, keyword }) => {
  if (keyword == null || keyword == undefined) {
    return null;
  }
  const index = keyword.lastIndexOf(".");
  if (index > -1) {
    keyword = keyword.slice(0, index);
  }
  return await request({
    url: "/api/v1/pan/recommend",
    params: {
      keyword,
      ip,
    },
  });
};

export const getDetail = async ({ id, size = 15, ip }) => {
  return await request({
    url: "/api/v1/pan/detail",
    params: {
      id: id,
      size: size,
      ip,
    },
    headers: {
      "X-Authorization": process.server ? "" : localStorage.getItem("token"),
    },
  });
};

export const getUrl = async ({ id }) => {
  return await request({
    url: "/api/v1/pan/detail/url",
    params: { id: id },
  });
};

export const checkUrlFromBaidu = async (data) => {
  return (
    (await request({
      url: "/api/v1/pan/checkUrlValidFromBaidu",
      params: { data },
    })) || {}
  );
};

export const getRecommandWords = async () => {
  return HOTWORDS;
};

export const getFriendLinks = async () => {
  return LINKS;
};

export const getAdsInfo = async () => {
  return await request({
    isPrefix: false,
    url: `https://res.oodcd.cn/pan/config/ad.json`,
  });
};

export const getFooterAdsInfo = async () => {
  return await request({
    isPrefix: false,
    url: `https://res.oodcd.cn/pan/config/ad_footer.json`,
  });
};

export const getKeywordAdsInfo = async () => {
  return await request({
    isPrefix: false,
    url: `https://res.oodcd.cn/pan/config/ad_keyword.json`,
  });
};

export const getCopyContent = async () => {
  return await request({
    isPrefix: false,
    url: `https://res.oodcd.cn/pan/config/copy.json`,
  });
};

export const getBlockedHistory = async () => {
  return await request({
    isPrefix: false,
    url: `https://res.oodcd.cn/pan/config/history.json`,
  });
};

export const getGroupInfo = async () => {
  return await request({
    isPrefix: false,
    url: `https://res.oodcd.cn/pan/config/group.json`,
  });
};

export const getFeisuxiaConfig = async () => {
  return await request({
    isPrefix: false,
    url: `https://dl.feisuxia.com/release/release.json`,
  });
};
