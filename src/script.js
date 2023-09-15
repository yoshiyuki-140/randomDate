// ロケーションデータ
let locations = {
    "https://youtu.be/7HgJIAUtICU?si=Y2PXl4UDJJaiZkWP": [
        "中村記念館",
        "安江金箔工芸館",
        "能楽美術館"
    ],
    "": [

    ],
    "": [

    ],
};

// 文字列からJSON形式のデータを取得する
let url = "https://youtu.be/7HgJIAUtICU?si=Y2PXl4UDJJaiZkWP";
const number_of_dest = 3;

function getLocationFromURLstr() {
    let num = Math.floor(Math.random() * number_of_dest);
    let canvas = document.getElementById('canvas');
    canvas.textContent = locations[url][num];
}

// getLocationFromURLstr()のラッパーコード
function execute() {
    let url = "https://youtu.be/7HgJIAUtICU?si=Y2PXl4UDJJaiZkWP";
    getLocationFromURLstr(url);
}
