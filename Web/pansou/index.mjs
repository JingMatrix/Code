// Usage: node index.mjs [search keyword]
//
//
import { createInterface } from "readline";
import { getSearchResult, getDetail } from "./search.mjs";

let file = {};
let results = [];
let data = {
  size: -1,
  type: -1,
  time: -1,
  searchtype: -1,
  page: 1,
  keyword: "",
};
const print_step = 3;
const rl = createInterface({
  input: process.stdin,
  output: process.stdout,
});

if (!process.argv[2]) {
  console.log("Usage: node index.mjs [search keyword]");
  process.exit();
}

// main enter point, start user interface
main(process.argv[2]);

async function main(keyword) {
  await search(keyword);
  show_result();
  user_interface();
  // Load one more page to save some time
  // loadpage += 1;
  // search(keyword, loadpage);
}

async function search(kw) {
  data.keyword = kw;
  let lists = await getSearchResult(data);
  results = results.concat(lists.resources.filter(unique_filter));
}

function unique_filter(entry) {
  if (file[entry.res.filename]) {
    return false;
  }
  file[entry.res.filename] = true;
  return true;
}

function print_title(index, result) {
  console.log(index + "\t" + result.res.filename);
}

function print_content(result) {
  if (result.res.filelist) {
    for (const file of result.res.filelist) console.log("\t\t" + file.filename);
  }
}

async function print_url(index) {
  const info = results[index].res;
  console.log("Finding share url...");
  if (info.id !== "login_first") {
    let detail = await getDetail(info.id);
    if (detail.haspwd) {
      console.log("Password to this share link is:\t" + detail.pwd);
    } else {
      console.log("This share link has no password");
    }
    console.log(detail.url);
  } else {
    console.log("Fail to get id for now");
    console.log("You must login, and put login token in search.mjs");
  }
  rl.prompt();
}

function show_result(index, length = print_step) {
  let start = index >= 0 ? index : 0;
  let end = start + length <= results.length ? start + length : results.length;
  for (let pos = start; pos < end; pos++) {
    const result = results[pos];
    // console.log(result)
    print_title(pos, result);
    print_content(result);
  }
}

function user_interface() {
  let index = 0;
  rl.setPrompt("Command> ");
  rl.prompt();
  rl.on("line", (line) => {
    if (isNaN(line)) {
      switch (line) {
        case "n":
          index += print_step;
          if (index < results.length) {
            show_result(index);
          } else {
            console.log("Loading more result... Try again later");
            loadpage += 1;
            search(process.argv[2], loadpage);
            index = results.length;
            index -= print_step;
          }
          break;
        case "p":
          index -= print_step;
          if (index >= 0) {
            show_result(index);
          } else {
            console.log("try n command");
            index = 0;
          }
          break;
        default:
          console.log(
            `n:\tNext ${print_step} result\np:\tPrevious ${print_step} result\nNumber:\tInfo for that entry`
          );
      }
      rl.prompt();
    } else {
      index = +line;
      print_url(index);
    }
  }).on("close", () => {
    console.log("Have a nice day");
    process.exit(0);
  });
}
