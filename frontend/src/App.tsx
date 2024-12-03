import { useState, useEffect, useMemo } from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { HelmetProvider, Helmet } from 'react-helmet-async';
import { ThemeProvider } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';
import ReactGA from 'react-ga4';

import getTheme from './theme/theme';
import ColorModeContext from './utils/ColorModeContext';
import Layout from './layout/Layout';
import Home from './pages/Home';
import Signup from './pages/Signup';
import Login from './pages/Login';
import StripePricing from './pages/PricingTable';


const NotFound = () => {
  return (
    <div style={{ textAlign: 'center', marginTop: '20vh' }}>
      <h3>404 - Not found</h3>
    </div>
    );
};


const App = (): JSX.Element => {
  const [mode, setMode] = useState('light');
  const colorMode = useMemo(
    () => ({
      // The theme mode switch will invoke this method
      toggleColorMode: () => {
        window.localStorage.setItem(
          'themeMode',
          mode === 'dark' ? 'light' : 'dark'
        );
        setMode((prevMode) => (prevMode === 'dark' ? 'light' : 'dark'));
      },
    }),
    [mode]
  );

  useEffect(() => {
    try {
      const localTheme = window.localStorage.getItem('themeMode');
      localTheme ? setMode(localTheme) : setMode('light');
    } catch {
      setMode('light');
    }

    // Initialize react-ga and track the initial pageview
    ReactGA.initialize('YOUR-GOOGLE-ANALYTICS-MEASUREMENT-ID');
    ReactGA.send({ hitType: 'pageview', page: window.location.pathname + window.location.search });

  }, []);

  return (
    <HelmetProvider>
      <Helmet
        titleTemplate="%s | Data Dynamo"
        defaultTitle="Data Dynamo | No Data No Business"
      />
      <ColorModeContext.Provider value={colorMode}>
        <ThemeProvider theme={getTheme(mode)}>
          <CssBaseline />
          <BrowserRouter>
            <Layout>
              <Routes>
                <Route path='/' element={<Home />} />
                <Route path="/signup" element={<Signup />} />
                <Route path="/login" element={<Login />} />
                <Route path="/pricing-table" element={<StripePricing />} />
                <Route path="*" element={<NotFound />} />
              </Routes>
            </Layout>
          </BrowserRouter>
        </ThemeProvider>
      </ColorModeContext.Provider>
    </HelmetProvider>
  );
};

export default App;
