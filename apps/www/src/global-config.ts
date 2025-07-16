import packageJson from '../package.json';

// ----------------------------------------------------------------------

export type ConfigValue = {
  appVersion: string;
  apiBaseUrl: string; // TODO: Move to env variable
};

// ----------------------------------------------------------------------

export const CONFIG: ConfigValue = {
  appVersion: packageJson.version,
  apiBaseUrl: 'http://localhost:8080/api/'
};