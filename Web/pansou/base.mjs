// Possible api for now
//
// https://api.feizhupan.com
// https://api.iizhi.cn
// https://api.luomapan.com/
// https://api.dashengpan.com/
// https://api.dalipan.com/
// https://api.xiaomapan.com/
import axios from "axios";
const APIHOST = "https://api.dalipan.com";

export const request = async ({
  method = "GET",
  data,
  url,
  params = {},
  headers = {},
  isPrefix = true,
}) => {
  try {
    if (method.toLowerCase() === "post") {
      params._post = JSON.stringify(data);
      data = undefined;
      method = "GET";
    }
    const res = await axios({
      method,
      url: isPrefix ? `${APIHOST}${url}` : url,
      data,
      timeout: 20 * 1000,
      params: {
        t: new Date().getTime(),
        ...params,
      },
      headers: {
        ...headers,
      },
    });
    return res.data;
  } catch (err) {
    console.log(`request error: ${err}`);
    return null;
  }
};
