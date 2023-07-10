const puppeteer = require('puppeteer');
const StealthPlugin = require('puppeteer-extra-plugin-stealth');
const cheerio = require('cheerio');

const proxyUrl = 'http://39.62.7.232:8080';
const targetUrl = 'https://qalam.nust.edu.pk/';
const username = 'username';
const password = 'pass';

(async () => {

  const browser = await puppeteer.launch({headless: false});
  const page = await browser.newPage();
  
  await page.goto(targetUrl, {timeout: 60000});

  await page.type('input[name="login"]', username);
  await page.type('input[name="password"]', password);
  await page.click('.btn.btn-nust.btn-block.py-3.mt-4');

  // await page.waitForSelector('#user_heading_content', {timeout: 60000});

  await page.waitForSelector('div.user_heading_content', { timeout: 30000 });

  const html = await page.content();

  const cookies = await page.cookies();

  const $ = cheerio.load(html);

  // Perform scraping operations using Cheerio
  const elementText = $('h2.heading_b').text();

  console.log(elementText);

  await browser.close();
})();
