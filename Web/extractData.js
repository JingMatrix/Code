import { createInterface } from "readline";
import { get } from "https";

const rl = createInterface({
	input: process.stdin,
	output: process.stdout,
});

let file = {};
let results = __NUXT__.data[0].results.filter(unique_filter);

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

function get_url(index) {
	// console.log(results[index].res);
	const info = results[index].res;
	if (info.haspwd) {
		console.log("Password to this share link is:\t" + info.pwd);
	} else {
		console.log("This share link has no password");
	}
	console.log("Finding share url...");
	let url = "https://www.feizhupan.com/api/detail?id=" + info.id;
	let req = get(url, function (res) {
		let data = "",
			json_data;

		res.on("data", function (stream) {
			data += stream;
		});
		res.on("end", function () {
			json_data = JSON.parse(data);

			// will output a Javascript object
			console.log(json_data.url);
			rl.prompt();
		});
	});

	req.on("error", function (e) {
		console.log(e.message);
	});
}

const print_step = 3;

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

let index = 0;
show_result();
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
					console.log("try p command");
					index = results.length;
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
		get_url(index);
	}
}).on("close", () => {
	console.log("Have a nice day");
	process.exit(0);
});
