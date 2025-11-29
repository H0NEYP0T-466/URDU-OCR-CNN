/**
 * Footer Component
 * 
 * Application footer with links and copyright.
 */

interface FooterProps {
  year?: number;
}

const Footer: React.FC<FooterProps> = ({ year = new Date().getFullYear() }) => {
  return (
    <footer className="bg-gray-800 text-gray-300 mt-auto">
      <div className="container mx-auto px-4 py-8">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          {/* About */}
          <div>
            <h3 className="text-white font-semibold mb-3">Urdu OCR</h3>
            <p className="text-sm">
              A deep learning-powered application for recognizing handwritten Urdu characters
              using Convolutional Neural Networks.
            </p>
          </div>

          {/* Quick Links */}
          <div>
            <h3 className="text-white font-semibold mb-3">Quick Links</h3>
            <ul className="space-y-2 text-sm">
              <li>
                <a href="https://github.com" className="hover:text-white transition-colors" target="_blank" rel="noopener noreferrer">
                  GitHub Repository
                </a>
              </li>
              <li>
                <a href="/docs" className="hover:text-white transition-colors">
                  API Documentation
                </a>
              </li>
              <li>
                <a href="/about" className="hover:text-white transition-colors">
                  About the Project
                </a>
              </li>
            </ul>
          </div>

          {/* Technology */}
          <div>
            <h3 className="text-white font-semibold mb-3">Technology</h3>
            <div className="flex flex-wrap gap-2">
              {['React', 'FastAPI', 'TensorFlow', 'TypeScript'].map((tech) => (
                <span
                  key={tech}
                  className="px-2 py-1 bg-gray-700 rounded text-xs"
                >
                  {tech}
                </span>
              ))}
            </div>
          </div>
        </div>

        {/* Copyright */}
        <div className="border-t border-gray-700 mt-8 pt-6 text-center text-sm">
          <p>© {year} Urdu OCR. Built with ❤️ for the Urdu language.</p>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
