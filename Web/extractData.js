for (const result of data.data[0].results) {
	console.log(result.res.filename);
	// console.log(result.res.id);
	if (result.res.filelist) {
		for (const file of result.res.filelist) console.log("\t\t" + file.filename);
	}
}
