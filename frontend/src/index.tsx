import ReactDOM from 'react-dom/client';
import App from './App';
import { AuthProvider } from './AuthContext';

const root = ReactDOM.createRoot(
  document.getElementById('root') as HTMLElement
);

root.render(
  <AuthProvider>
    <App />
  </AuthProvider>
);
