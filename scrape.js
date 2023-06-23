const puppeteer = require('puppeteer');
const cheerio = require('cheerio');

const proxyUrl = 'http://39.62.7.232:8080';
const targetUrl = 'https://qalam.nust.edu.pk/';
const username = 'mkaleem.bscs22seecs';
const password = 'ILIPtphi180M!';

(async () => {
  const browser = await puppeteer.launch({headless: false});
  // const browser = await puppeteer.launch({ args: [`--proxy-server=${proxyUrl}`] });
  const page = await browser.newPage();
  
  await page.goto(targetUrl, {timeout: 60000});

  await page.type('input[name="login"]', username);
  await page.type('input[name="password"]', password);
  await page.click('.btn.btn-nust.btn-block.py-3.mt-4');

  // Modify the code to wait for a specific element to appear after login
  await page.waitForSelector('#user_heading_content');

  const html = await page.content();

  const $ = cheerio.load(html);

  // Perform scraping operations using Cheerio
  // Example: Extract the text content of a specific element
  const elementText = $('#user_heading_content').text();

  console.log(elementText);

  await browser.close();
})();
