// Google Apps Script - 이미지 영상 제작기
// 브라우저에서 직접 MP4로 녹화 (변환 API 불필요)

function doGet() {
  return HtmlService.createTemplateFromFile('index')
    .evaluate()
    .setTitle('이미지 영상 제작기')
    .setFaviconUrl('https://www.google.com/favicon.ico')
    .addMetaTag('viewport', 'width=device-width, initial-scale=1.0')
    .setXFrameOptionsMode(HtmlService.XFrameOptionsMode.ALLOWALL);
}

// HTML 파일 포함
function include(filename) {
  return HtmlService.createHtmlOutputFromFile(filename).getContent();
}

