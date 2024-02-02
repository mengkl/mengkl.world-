//[公共] 初始随机字符范围
const src = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+-=[]{}|;:,.<>?';

// 0
let randomStr0 = randomString(target0.length, src);
RandomNum(target0, randomStr0, 0, "numbers0")
// 1
let randomStr1 = randomString(target1.length, src);
RandomNum(target1, randomStr1, 0, "numbers1")
// 2
const target2 = "223456789"
let randomStr2 = randomString(target2.length, src);
RandomNum(target2, randomStr2, 0, "numbers2")

//[公共]生成初始随机字符串
function randomString(length, chars) {
    let result = '';
    for (let i = length; i > 0; --i) result += chars[Math.floor(Math.random() * chars.length)];
    return result;
}

// [公共]随机数字函数
function RandomNum(target, randomStr, count, htmlid) {
    setInterval(async () => {
        if (count < target.length) {
            // 多次切换随机字符
            for (let i = 0; i < 5; i++) {
                let randomChar = String.fromCharCode(Math.floor(Math.random() * 94) + 33);
                randomStr = replaceChar(randomStr, count, randomChar);
                document.getElementById(htmlid).textContent = randomStr;
                await sleep(100);
            }

            // 最后替换为目标字符
            randomStr = replaceChar(randomStr, count, target[count]);
            document.getElementById(htmlid).textContent = randomStr;
            count++;
        }
    }, 500);
}

// [公共]替换指定位置的字符
function replaceChar(str, index, newChar) {
    return str.substring(0, index) + newChar + str.substring(index + 1);
}

// [公共]暂停函数
function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}