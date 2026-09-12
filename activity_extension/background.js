const sites = {
    "leetcode.com": "LC",
    "hackerrank.com": "HR",
    "skillrack.com": "SR",
    "codechef.com": "CC",
    "codeforces.com": "CF"
};

// Use this while testing locally
const API_URL = "http://127.0.0.1:8000/api/leetcode-activity/";

let activeSite = null;
let startTime = null;


function getSite(url) {
    if (!url) return null;

    try {
        const hostname = new URL(url).hostname.replace("www.", "");

        for (const domain in sites) {
            if (hostname === domain || hostname.endsWith("." + domain)) {
                return sites[domain];
            }
        }
    } catch (error) {
        return null;
    }

    return null;
}


function getToday() {
    const now = new Date();

    return (
        now.getFullYear() + "-" +
        String(now.getMonth() + 1).padStart(2, "0") + "-" +
        String(now.getDate()).padStart(2, "0")
    );
}


async function saveCurrentTime() {
    if (!activeSite || !startTime) return;

    const seconds = (Date.now() - startTime) / 1000;

    const today = getToday();

    const data = await chrome.storage.local.get(today);

    const activity = data[today] || {
        LC: 0,
        HR: 0,
        SR: 0,
        CC: 0,
        CF: 0
    };

    activity[activeSite] += seconds;

    await chrome.storage.local.set({
        [today]: activity
    });

    startTime = Date.now();
}


async function sendActivityToLifeOS() {
    const today = getToday();

    const data = await chrome.storage.local.get(today);

    const activity = data[today] || {
        LC: 0,
        HR: 0,
        SR: 0,
        CC: 0,
        CF: 0
    };

    // Convert seconds → minutes
    const minutes = {
        LC: activity.LC / 60,
        HR: activity.HR / 60,
        SR: activity.SR / 60,
        CC: activity.CC / 60,
        CF: activity.CF / 60
    };

    try {
        const response = await fetch(API_URL, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(minutes)
        });

        const result = await response.json();

        console.log("LifeOS updated:", result);

    } catch (error) {
        console.error("Could not send activity to LifeOS:", error);
    }
}


async function updateActiveTab() {
    await saveCurrentTime();
    await sendActivityToLifeOS();

    const tabs = await chrome.tabs.query({
        active: true,
        lastFocusedWindow: true
    });

    if (tabs.length === 0) {
        activeSite = null;
        startTime = null;
        return;
    }

    activeSite = getSite(tabs[0].url);

    if (activeSite) {
        startTime = Date.now();
    } else {
        startTime = null;
    }
}


chrome.tabs.onActivated.addListener(() => {
    updateActiveTab();
});


chrome.windows.onFocusChanged.addListener(() => {
    updateActiveTab();
});


chrome.tabs.onUpdated.addListener((tabId, changeInfo, tab) => {
    if (tab.active && changeInfo.url) {
        updateActiveTab();
    }
});


chrome.idle.onStateChanged.addListener((state) => {
    if (state === "active") {
        updateActiveTab();
    } else {
        saveCurrentTime();
        sendActivityToLifeOS();

        activeSite = null;
        startTime = null;
    }
});


chrome.alarms.create("saveActivity", {
    periodInMinutes: 1
});


chrome.alarms.onAlarm.addListener(async () => {
    await saveCurrentTime();
    await sendActivityToLifeOS();
});