// Usage: node 52pansou.mjs [search keyword]
//
// Possible api for now
//
// https://www.feizhupan.com
// https://www.iizhi.cn
//
// Encryted api, it hides share url behind $api/detail/url?id=
//
// But always return -1 for now
// https://www.luomapan.com/
// https://www.dashengpan.com/
// https://www.dalipan.com/
// https://www.xiaomapan.com/
//
import { createInterface } from "readline";
import { get } from "https";

let file = {};
let results = [];
let loadpage = 1;
const print_step = 3;
const api = "https://www.feizhupan.com/api/";
const rl = createInterface({
	input: process.stdin,
	output: process.stdout,
});

if (!process.argv[2]) {
	console.log("Usage: node 52pansou.mjs [search keyword]");
	process.exit();
}

// main enter point, start user interface
main(process.argv[2]);

async function main(keyword) {
	await search(keyword, loadpage);
	show_result();
	user_interface();
	// Load one more page to save some time
	// loadpage += 1;
	// search(keyword, loadpage);
}

async function search(kw, page = loadpage) {
	let url = api + "search?kw=" + kw + "&page=" + page;
	let lists = await get_json(encodeURI(url));
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
	let url = api + "detail?id=" + info.id;
	let detail = await get_json(url);
	if (detail.haspwd) {
		console.log("Password to this share link is:\t" + detail.pwd);
	} else {
		console.log("This share link has no password");
	}
	console.log(detail.url);
	rl.prompt();
}

function get_json(url) {
	return new Promise((resolve, reject) => {
		let req = get(url, function (res) {
			let data = "";
			res.on("data", function (stream) {
				data += stream;
			});
			res.on("end", function () {
				resolve(JSON.parse(data));
			});
		});
		req.on("error", function (e) {
			reject(e);
		});
	});
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
