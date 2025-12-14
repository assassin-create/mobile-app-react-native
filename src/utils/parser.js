// parser.js

import { console } from 'console';

class Parser {
  constructor(data) {
    this.data = data;
  }

  parseJson() {
    try {
      return JSON.parse(this.data);
    } catch (error) {
      console.error('Error parsing JSON:', error);
      return null;
    }
  }

  parseXml() {
    const parser = new DOMParser();
    const xmlDoc = parser.parseFromString(this.data, 'text/xml');
    return xmlDoc.documentElement;
  }
}

export default Parser;