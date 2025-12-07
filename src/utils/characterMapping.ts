/**
 * Character Mapping
 * 
 * Maps English character names to their Urdu Unicode equivalents
 */

export const characterToUrdu: { [key: string]: string } = {
  'alif': 'ا',
  'alif mad aa': 'آ',
  'ayn': 'ع',
  'baa': 'ب',
  'bari yaa': 'ے',
  'cheey': 'چ',
  'choti yaa': 'ی',
  'daal': 'د',
  'dhaal': 'ڈ',
  'faa': 'ف',
  'gaaf': 'گ',
  'ghain': 'غ',
  'haa1': 'ہ',
  'haa2': 'ح',
  'haa3': 'ھ',
  'hamza': 'ء',
  'jeem': 'ج',
  'kaaf': 'ک',
  'khaa': 'خ',
  'laam': 'ل',
  'meem': 'م',
  'noon': 'ن',
  'noonghunna': 'ں',
  'paa': 'پ',
  'qaaf': 'ق',
  'raa': 'ر',
  'rhraa': 'ڑ',
  'seen': 'س',
  'seey': 'ص',
  'sheen': 'ش',
  'swaad': 'ض',
  'taa': 'ت',
  'ttaa': 'ٹ',
  'twa': 'ط',
  'waw': 'و',
  'zaaa': 'ز',
  'zaal': 'ذ',
  'zhaa': 'ژ',
  'zwaa': 'ظ',
  'zwaad': 'ث',
};

export const digitToUrdu: { [key: string]: string } = {
  '0': '۰',
  '1': '۱',
  '2': '۲',
  '3': '۳',
  '4': '۴',
  '5': '۵',
  '6': '۶',
  '7': '۷',
  '8': '۸',
  '9': '۹',
};

/**
 * Get the formatted character display (name + symbol)
 * @param prediction - The predicted character name or digit
 * @param isDigit - Whether this is a digit prediction
 * @returns Formatted string with name and Urdu character
 */
export const getFormattedCharacter = (prediction: string, isDigit: boolean = false): string => {
  if (isDigit) {
    const urduDigit = digitToUrdu[prediction];
    return urduDigit ? `${prediction} ${urduDigit}` : prediction;
  }
  
  const urduChar = characterToUrdu[prediction.toLowerCase()];
  return urduChar ? `${prediction} ${urduChar}` : prediction;
};

/**
 * Get all supported characters with their Urdu equivalents
 */
export const getAllCharacters = (): Array<{ name: string; urdu: string }> => {
  return Object.entries(characterToUrdu).map(([name, urdu]) => ({ name, urdu }));
};

/**
 * Get all supported digits with their Urdu equivalents
 */
export const getAllDigits = (): Array<{ name: string; urdu: string }> => {
  return Object.entries(digitToUrdu).map(([name, urdu]) => ({ name, urdu }));
};
