# API Passthrough For WeatherBit
class Weather():
    def __init__():
        pass

    def get_weather(data):
    #daily - standard (weatherbit)
        for count, item in enumerate(data['data']):
            code = str(item['weather']['code'])
            code = code + 'd'
            weathercode = WEATHER_CODES[code]
            set_property('Day%i.Title'              % count, convert_datetime(item['ts'], 'timestamp', 'weekday', 'long'))
            set_property('Day%i.HighTemp'           % count, str(int(round(item['max_temp']))))
            set_property('Day%i.LowTemp'            % count, str(int(round(item['min_temp']))))
            set_property('Day%i.Outlook'            % count, FORECAST.get(item['weather']['code'], item['weather']['description']))
            set_property('Day%i.OutlookIcon'        % count, '%s.png' % weathercode)
            set_property('Day%i.FanartCode'         % count, weathercode)
            if count == MAXDAYS:
                break
    #daily - extended (weatherbit)
        for count, item in enumerate(data['data']):
            code = str(item['weather']['code'])
            code = code + 'd'
            weathercode = WEATHER_CODES[code]
            set_property('Daily.%i.LongDay'         % (count+1), convert_datetime(item['ts'], 'timestamp', 'weekday', 'long'))
            set_property('Daily.%i.ShortDay'        % (count+1), convert_datetime(item['ts'], 'timestamp', 'weekday', 'short'))
            set_property('Daily.%i.LongDate'        % (count+1), convert_datetime(item['ts'], 'timestamp', 'monthday', 'long'))
            set_property('Daily.%i.ShortDate'       % (count+1), convert_datetime(item['ts'], 'timestamp', 'monthday', 'short'))
            set_property('Daily.%i.Outlook'         % (count+1), FORECAST.get(str(item['weather']['code']), item['weather']['description']))
            set_property('Daily.%i.OutlookIcon'     % (count+1), WEATHER_ICON % weathercode)
            set_property('Daily.%i.FanartCode'      % (count+1), weathercode)
            set_property('Daily.%i.WindDirection'   % (count+1), xbmc.getLocalizedString(int(round(WIND_DIR(item['wind_dir'])))))
            set_property('Daily.%i.WindDegree'      % (count+1), str(item['wind_dir']) + u'°')
            set_property('Daily.%i.Humidity'        % (count+1), str(item['rh']) + '%')
            set_property('Daily.%i.Temperature'     % (count+1), convert_temp(item['temp'], 'C') + TEMPUNIT)
            set_property('Daily.%i.HighTemperature' % (count+1), convert_temp(item['max_temp'], 'C') + TEMPUNIT)
            set_property('Daily.%i.LowTemperature'  % (count+1), convert_temp(item['min_temp'], 'C') + TEMPUNIT)
            set_property('Daily.%i.FeelsLike'       % (count+1), convert_temp(int(round(item['app_max_temp'])), 'C') + TEMPUNIT)
            set_property('Daily.%i.HighFeelsLike'   % (count+1), convert_temp(int(round(item['app_max_temp'])), 'C') + TEMPUNIT)
            set_property('Daily.%i.LowFeelsLike'    % (count+1), convert_temp(int(round(item['app_min_temp'])), 'C') + TEMPUNIT)
            set_property('Daily.%i.DewPoint'        % (count+1), convert_temp(int(round(item['dewpt'])), 'C') + TEMPUNIT)
            if 'F' in TEMPUNIT:
                set_property('Daily.%i.Pressure'      % (count+1), str(round(item['pres'] / 33.86 ,2)) + ' in')
                set_property('Daily.%i.SeaLevel'      % (count+1), str(round(item['slp'] / 33.86 ,2)) + ' in')
                set_property('Daily.%i.Snow'          % (count+1), str(round(item['snow'] * 0.04 ,2)) + ' in')
                set_property('Daily.%i.SnowDepth'     % (count+1), str(round(item['snow_depth'] * 0.04 ,2)) + ' in')
                if item['precip']:
                    set_property('Daily.%i.Precipitation' % (count+1), str(round(item['precip'] * 0.04 ,2)) + ' in')
                else:
                    set_property('Daily.%i.Precipitation' % (count+1), '')
                set_property('Daily.%i.Visibility'    % (count+1), str(round(item['vis'] * 0.621371 ,2)) + ' mi')
            else:
                set_property('Daily.%i.Pressure'      % (count+1), str(item['pres']) + ' mb')
                set_property('Daily.%i.SeaLevel'      % (count+1), str(round(item['slp'])) + ' mb')
                set_property('Daily.%i.Snow'          % (count+1), str(round(item['snow'])) + ' mm')
                set_property('Daily.%i.SnowDepth'     % (count+1), str(round(item['snow_depth'])) + ' mm')
                if item['precip']:
                    set_property('Daily.%i.Precipitation' % (count+1), str(round(item['precip'])) + ' mm')
                else:
                    set_property('Daily.%i.Precipitation' % (count+1), '')
                set_property('Daily.%i.Visibility'    % (count+1), str(item['vis']) + ' km')
            set_property('Daily.%i.WindSpeed'         % (count+1), convert_speed(item['wind_spd'], 'mps') + SPEEDUNIT)
            set_property('Daily.%i.WindGust'          % (count+1), convert_speed(item['wind_gust_spd'], 'mps') + SPEEDUNIT)
            set_property('Daily.%i.Cloudiness'        % (count+1), str(item['clouds']) + '%')
            set_property('Daily.%i.CloudsLow'         % (count+1), str(item['clouds_low']) + '%')
            set_property('Daily.%i.CloudsMid'         % (count+1), str(item['clouds_mid']) + '%')
            set_property('Daily.%i.CloudsHigh'        % (count+1), str(item['clouds_hi']) + '%')
            set_property('Daily.%i.Probability'       % (count+1), str(item['pop']) + '%')
            if item['uv']:
                set_property('Daily.%i.UVIndex'       % (count+1), str(int(round(item['uv']))) + '%')
            else:
                set_property('Daily.%i.UVIndex'       % (count+1), '')
            set_property('Daily.%i.Sunrise'           % (count+1), convert_datetime(item['sunrise_ts'], 'timestamp', 'timedate', None))
            set_property('Daily.%i.Sunset'            % (count+1), convert_datetime(item['sunset_ts'], 'timestamp', 'timedate', None))
            set_property('Daily.%i.Moonrise'          % (count+1), convert_datetime(item['moonrise_ts'], 'timestamp', 'timedate', None))
            set_property('Daily.%i.Moonset'           % (count+1), convert_datetime(item['moonset_ts'], 'timestamp', 'timedate', None))
            set_property('Daily.%i.MoonPhase'         % (count+1), str(item['moon_phase']))
            if item['ozone']:
                set_property('Daily.%i.Ozone'         % (count+1), str(int(round(item['ozone']))) + ' DU')
            else:
                set_property('Daily.%i.Ozone'         % (count+1), '')
        set_property('Daily.IsFetched'                , 'true')

# For Yahoo
class Weather():
    def __init__():
        pass

    def get_weather(response, loc, locid):
        try: #TODO temp workaround, can be removed in future versions
            data = response['weathers'][0]
        except:
            ADDON.setSettingString('ystamp', '') #this will force multiweather to retrieve a new crumb next time
            return
    #current - standard
        set_property('Location'                  , loc)
        set_property('Updated'                   , convert_datetime(data['observation']['observationTime']['timestamp'], 'datetime', 'timedate', None))
        set_property('Current.Location'          , data['location']['displayName'])
        set_property('Current.Condition'         , data['observation']['conditionDescription'])
        set_property('Current.Temperature'       , convert_temp(data['observation']['temperature']['now'], 'F', 'C'))
        set_property('Current.UVIndex'           , str(data['observation']['uvIndex']))
        set_property('Current.OutlookIcon'       , '%s.png' % str(data['observation']['conditionCode'])) # Kodi translates it to Current.ConditionIcon
        set_property('Current.FanartCode'        , str(data['observation']['conditionCode']))
        set_property('Current.Wind'              , convert_speed(data['observation']['windSpeed'], 'mph', 'kmh'))
        set_property('Current.WindDirection'     , xbmc.getLocalizedString(WIND_DIR(data['observation']['windDirection'])))
        set_property('Current.Humidity'          , str(data['observation']['humidity']))
        set_property('Current.DewPoint'          , dewpoint(int(convert_temp(data['observation']['temperature']['now'], 'F', 'C')), data['observation']['humidity']))
        set_property('Current.FeelsLike'         , convert_temp(data['observation']['temperature']['feelsLike'], 'F', 'C'))
    #current - extended
        set_property('Current.WindChill'         , convert_temp(windchill(data['observation']['temperature']['now'], data['observation']['windSpeed']), 'F') + TEMPUNIT)
        if 'F' in TEMPUNIT:
            set_property('Current.Visibility'    , str(round(data['observation']['visibility'],2)) + ' mi')
            set_property('Current.Pressure'      , str(round(data['observation']['barometricPressure'],2)) + ' inHg')
        else:
            set_property('Current.Visibility'    , str(round(1.60934 * data['observation']['visibility'],2)) + ' km')
            set_property('Current.Pressure'      , str(int(round((33.864 * data['observation']['barometricPressure'])))) + ' mbar')
        if 'precipitationProbability' in data['observation']:
            set_property('Current.Precipitation' , str(data['observation']['precipitationProbability']) + '%')
        set_property('Current.IsFetched'         , 'true')
    #forecast - extended
        set_property('Forecast.City'            , data['location']['displayName'])
        set_property('Forecast.Country'         , data['location']['countryName'])
        set_property('Forecast.Latitude'        , str(data['location']['latitude']))
        set_property('Forecast.Longitude'       , str(data['location']['longitude']))
        set_property('Forecast.Updated'         , convert_datetime(data['observation']['observationTime']['timestamp'], 'datetime', 'timedate', None))
        set_property('Forecast.IsFetched'       , 'true')
    #today - extended
        set_property('Today.Sunrise'             , convert_datetime(data['sunAndMoon']['sunrise'], 'seconds', 'time', None))
        set_property('Today.Sunset'              , convert_datetime(data['sunAndMoon']['sunset'], 'seconds', 'time', None))
        set_property('Today.Moonphase'           , MOONPHASE[data['sunAndMoon']['moonPhase']])
        set_property('Today.IsFetched'           , 'true')
    #hourly - extended
        for count, item in enumerate(data['forecasts']['hourly']):
            set_property('Hourly.%i.Time'            % (count + 1), convert_datetime(item['observationTime']['timestamp'], 'datetime', 'time', None))
            set_property('Hourly.%i.LongDate'        % (count + 1), convert_datetime(item['observationTime']['timestamp'], 'datetime', 'monthday', 'long'))
            set_property('Hourly.%i.ShortDate'       % (count + 1), convert_datetime(item['observationTime']['timestamp'], 'datetime', 'monthday', 'short'))
            set_property('Hourly.%i.Temperature'     % (count + 1), convert_temp(item['temperature']['now'], 'F') + TEMPUNIT)
            set_property('Hourly.%i.FeelsLike'       % (count + 1), convert_temp(item['temperature']['feelsLike'], 'F') + TEMPUNIT)
            set_property('Hourly.%i.Outlook'         % (count + 1), OUTLOOK.get(str(item['conditionCode']), str(item['conditionDescription'])))
            set_property('Hourly.%i.OutlookIcon'     % (count + 1), '%s.png' % str(item['conditionCode']))
            set_property('Hourly.%i.FanartCode'      % (count + 1), str(item['conditionCode']))
            set_property('Hourly.%i.Humidity'        % (count + 1), str(item['humidity']) + '%')
            set_property('Hourly.%i.Precipitation'   % (count + 1), str(item['precipitationProbability']) + '%')
            set_property('Hourly.%i.WindDirection'   % (count + 1), xbmc.getLocalizedString(WIND_DIR(item['windDirection'])))
            set_property('Hourly.%i.WindSpeed'       % (count + 1), convert_speed(item['windSpeed'], 'mph') + SPEEDUNIT)
            set_property('Hourly.%i.WindDegree'      % (count + 1), str(item['windDirection']) + u'°')
            set_property('Hourly.%i.DewPoint'        % (count + 1), convert_temp(dewpoint(int(convert_temp(item['temperature']['now'], 'F', 'C')), item['humidity']), 'C') + TEMPUNIT)
        set_property('Hourly.IsFetched'              , 'true')

    def get_daily_weather(response):
        try: #TODO temp workaround, can be removed in future versions
            data = response['weathers'][0]
        except:
            return
    #daily - standard
        for count, item in enumerate(data['forecasts']['daily']):
            set_property('Day%i.Title'           % count, convert_datetime(item['observationTime']['weekday'], 'day', 'weekday', 'long'))
            set_property('Day%i.HighTemp'        % count, convert_temp(item['temperature']['high'], 'F', 'C'))
            set_property('Day%i.LowTemp'         % count, convert_temp(item['temperature']['low'], 'F', 'C'))
            set_property('Day%i.Outlook'         % count, item['conditionDescription'])
            set_property('Day%i.OutlookIcon'     % count, '%s.png' % str(item['conditionCode']))
            set_property('Day%i.FanartCode'      % count, str(item['conditionCode']))
            if count == MAXDAYS:
                break
    #daily - extended
        for count, item in enumerate(data['forecasts']['daily']):
            set_property('Daily.%i.ShortDay'        % (count + 1), convert_datetime(item['observationTime']['weekday'], 'day', 'weekday', 'short'))
            set_property('Daily.%i.LongDay'         % (count + 1), convert_datetime(item['observationTime']['weekday'], 'day', 'weekday', 'long'))
            set_property('Daily.%i.ShortDate'       % (count + 1), convert_datetime(item['observationTime']['timestamp'], 'datetime', 'monthday', 'short'))
            set_property('Daily.%i.LongDate'        % (count + 1), convert_datetime(item['observationTime']['timestamp'], 'datetime', 'monthday', 'long'))
            set_property('Daily.%i.HighTemperature' % (count + 1), convert_temp(item['temperature']['high'], 'F') + TEMPUNIT)
            set_property('Daily.%i.LowTemperature'  % (count + 1), convert_temp(item['temperature']['low'], 'F') + TEMPUNIT)
            set_property('Daily.%i.Outlook'         % (count + 1), OUTLOOK.get(str(item['conditionCode']), str(item['conditionDescription'])))
            set_property('Daily.%i.OutlookIcon'     % (count + 1), '%s.png' % str(item['conditionCode']))
            set_property('Daily.%i.FanartCode'      % (count + 1), str(item['conditionCode']))
            set_property('Daily.%i.Humidity'        % (count + 1), str(item['humidity']) + '%')
            set_property('Daily.%i.Precipitation'   % (count + 1), str(item['precipitationProbability']) + '%')
            set_property('Daily.%i.DewPoint'        % (count + 1), convert_temp(dewpoint(int(convert_temp(item['temperature']['low'], 'F', 'C')), item['humidity']), 'C') + TEMPUNIT)
        set_property('Daily.IsFetched'              , 'true')
# Weathermaps (if time allots)
class Weather():
    def __init__():
        pass

    def get_weather(lat, lon, zoom, mapid):
        if xbmc.getCondVisibility('System.HasAddon(script.openweathermap.maps)'):
            xbmc.executebuiltin('RunAddon(script.openweathermap.maps,lat=%s&lon=%s&zoom=%s&api=%s&debug=%s)' % (lat, lon, zoom, mapid, DEBUG))
        else:
            set_property('Map.IsFetched', '')
            for count in range (1, 6):
                set_property('Map.%i.Layer' % count, '')
                set_property('Map.%i.Area' % count, '')
                set_property('Map.%i.Heading' % count, '')
                set_property('Map.%i.Legend' % count, '')

#Gismeteo
from resources.libs import Gismeteo, GismeteoError, Location, Weather, WebClientError

weather = Weather()
_ = weather.initialize_gettext()

MAX_DAYS = 7
MAX_DAILYS = 7
MAX_LOCATIONS = 5
MAX_HOURLY = 16
MAX_36HOUR = 3
MAX_WEEKENDS = 2

WEATHER_ICON = weather.weather_icon

CURRENT_TIME = {'unix': time.time()}


def set_item_info(props, item, item_type, icon='%s.png', day_temp=None):
    keys = list(props.keys())

    # Date
    date = item['date']

    if 'Title' in keys:
        props['Title'] = weather.get_weekday(date, 'l')

    if 'Time' in keys:
        props['Time'] = weather.get_time(date)

    if 'LongDay' in keys:
        props['LongDay'] = weather.get_weekday(date, 'l')

    if 'ShortDay' in keys:
        props['ShortDay'] = weather.get_weekday(date, 's')

    if 'LongDate' in keys:
        form = 'dl' if (weather.DATEFORMAT[1] == 'd' or weather.DATEFORMAT[0] == 'D') else 'ml'
        props['LongDate'] = weather.get_month(date, form)

    if 'ShortDate' in keys:
        form = 'ds' if (weather.DATEFORMAT[1] == 'd' or weather.DATEFORMAT[0] == 'D') else 'ms'
        props['ShortDate'] = weather.get_month(date, form)

    # Outlook
    weather_code = weather.get_weather_code(item)

    if 'Outlook' in keys:
        props['Outlook'] = item['description']

    if 'Condition' in keys:
        props['Condition'] = item['description']

    if 'OutlookIcon' in keys:
        props['OutlookIcon'] = icon % weather_code

    if 'FanartCode' in keys:
        props['FanartCode'] = weather_code

    if 'ProviderIcon' in keys \
            and weather.use_provider_icon:
        props['ProviderIcon'] = 'resource://resource.images.weatherprovidericons.gismeteo/{0}.png'.format(item['icon'])

    # Wind

    wind = item['wind']

    speed = 0
    if isinstance(wind['speed'], dict):
        speed = wind['speed']['avg']
    elif isinstance(wind['speed'], float):
        speed = wind['speed']

    if 'Wind' in keys:
        props['Wind'] = int(round(speed * 3.6))

    if 'WindSpeed' in keys:
        props['WindSpeed'] = '{0} {1}'.format(weather.SPEED(speed), _(weather.SPEEDUNIT))

    if 'WindDirection' in keys:
        props['WindDirection'] = weather.get_wind_direction(wind['direction'])

    if 'MaxWind' in keys:
        props['MaxWind'] = '{0} {1}'.format(weather.SPEED(wind['speed']['max']), _(weather.SPEEDUNIT))

    # Temperature

    if 'DewPoint' in keys and item_type == 'day':
        props['DewPoint'] = weather.DEW_POINT(item['temperature']['max'], item['humidity']['avg']) + weather.TEMPUNIT
    elif 'DewPoint' in keys and item_type == 'hour':
        props['DewPoint'] = weather.DEW_POINT(item['temperature']['air'], item['humidity']) + weather.TEMPUNIT
    elif 'DewPoint' in keys and item_type == 'cur':
        props['DewPoint'] = weather.DEW_POINT(item['temperature']['air'], item['humidity'], False)

    if 'HighTemp' in keys:
        props['HighTemp'] = '{0}'.format(item['temperature']['max'])

    if 'LowTemp' in keys:
        props['LowTemp'] = '{0}'.format(item['temperature']['min'])

    if 'HighTemperature' in keys:
        props['HighTemperature'] = weather.TEMP(item['temperature']['max']) + weather.TEMPUNIT

    if 'HighTemperature' in keys:
        props['LowTemperature'] = weather.TEMP(item['temperature']['min']) + weather.TEMPUNIT

    if 'Temperature' in keys and item_type == 'cur':
        props['Temperature'] = item['temperature']['air']
    elif 'Temperature' in keys:
        props['Temperature'] = weather.TEMP(item['temperature']['air']) + weather.TEMPUNIT

    if 'FeelsLike' in keys and item_type == 'cur':
        props['FeelsLike'] = item['temperature']['comfort']
    elif 'FeelsLike' in keys:
        props['FeelsLike'] = weather.TEMP(item['temperature']['comfort']) + weather.TEMPUNIT

    if day_temp is not None:
        if 'TempMorn' in keys \
                and day_temp.get('morn') is not None:
            props['TempMorn'] = weather.TEMP(day_temp['morn']) + weather.TEMPUNIT
        if 'TempDay' in keys \
                and day_temp.get('day') is not None:
            props['TempDay'] = weather.TEMP(day_temp['day']) + weather.TEMPUNIT
        if 'TempEve' in keys \
                and day_temp.get('eve') is not None:
            props['TempEve'] = weather.TEMP(day_temp['eve']) + weather.TEMPUNIT
        if 'TempNight' in keys \
                and day_temp.get('night') is not None:
            props['TempNight'] = weather.TEMP(day_temp['night']) + weather.TEMPUNIT

    # Humidity

    if 'Humidity' in keys:
        humidity = item['humidity']['avg'] if item_type == 'day' else item['humidity']
        tpl = '{0}%' if item_type != 'cur' else '{0}'
        props['Humidity'] = tpl.format(humidity) if humidity is not None else _('n/a')

    if 'MinHumidity' in keys and item_type == 'day':
        humidity = item['humidity']['min']
        props['MinHumidity'] = '{0}%'.format(humidity) if humidity is not None else _('n/a')

    if 'MaxHumidity' in keys and item_type == 'day':
        humidity = item['humidity']['max']
        props['MaxHumidity'] = '{0}%'.format(humidity) if humidity is not None else _('n/a')

    # Pressure

    if 'Pressure' in keys:
        pressure = item['pressure']['avg'] if item_type == 'day' else item['pressure']
        props['Pressure'] = '{0} {1}'.format(weather.PRESSURE(pressure),
                                             _(weather.PRESUNIT)) if pressure is not None else _('n/a')

    # Precipitation

    if 'Precipitation' in keys:
        precip = item['precipitation']['amount']
        props['Precipitation'] = '{0} {1}'.format(weather.PRECIPITATION(precip),
                                                  _(weather.PRECIPUNIT)) if precip is not None else _('n/a')


def clear():
    # Current
    weather.set_properties(weather.prop_current(), 'Current')

    # Today
    weather.set_properties(weather.prop_today(), 'Today')

    # Forecast
    weather.set_properties(weather.prop_forecast(), 'Forecast')

    # Day
    day_props = weather.prop_day()
    for count in range(0, MAX_DAYS + 1):
        weather.set_properties(day_props, 'Day', count, '')

    # Daily
    daily_props = weather.prop_daily()
    for count in range(1, MAX_DAILYS + 1):
        weather.set_properties(daily_props, 'Daily', count)

    # Hourly
    hourly_props = weather.prop_hourly()
    for count in range(1, MAX_HOURLY + 1):
        weather.set_properties(hourly_props, 'Hourly', count)

    # Weekend
    for count in range(1, MAX_WEEKENDS + 1):
        weather.set_properties(daily_props, 'Weekend', count)

    # 36Hour
    _36hour_props = weather.prop_36hour()
    for count in range(1, MAX_36HOUR + 1):
        weather.set_properties(_36hour_props, '36Hour', count)


def refresh_locations():
    locations = 0
    if weather.get_setting('CurrentLocation'):
        try:
            lang = weather.gismeteo_lang()
            ip_locations = _ip_locations(lang)
        except (GismeteoError, WebClientError) as e:
            weather.notify_error(e)
            location = Location()
        else:
            for ip_location in ip_locations:
                location = Location(ip_location)
                break

        locations += 1
        weather.set_property('Location{0}'.format(locations), location.name)

    for count in range(1, MAX_LOCATIONS + 1):
        loc_name = weather.get_setting('Location{0}'.format(count))
        if loc_name:
            locations += 1
            weather.set_property('Location{0}'.format(locations), loc_name)

        elif not weather.get_setting('Location{0}ID'.format(count)):
            weather.set_setting('Location{0}ID'.format(count), '')

    weather.set_property('Locations', locations)


def set_location_props(forecast_info):
    count_days = 0
    count_hourly = 0
    count_36hour = 0
    count_weekends = 0

    # Current
    current_props = weather.prop_current()
    set_item_info(current_props, forecast_info['current'], 'cur')

    location_info = Location(forecast_info)
    current_props['Location'] = location_info.name

    weather.set_properties(current_props, 'Current')

    # Forecast
    forecast_props = weather.prop_forecast()
    forecast_props['City'] = forecast_info['name']
    forecast_props['Country'] = forecast_info['country']
    forecast_props['State'] = forecast_info['district']
    forecast_props['Latitude'] = forecast_info['lat']
    forecast_props['Longitude'] = forecast_info['lng']
    forecast_props['Updated'] = weather.convert_date(forecast_info['cur_time'])

    weather.set_properties(forecast_props, 'Forecast')

    # Today
    today_props = weather.prop_today()
    if forecast_info['current']['sunrise']['unix'] != forecast_info['current']['sunset']['unix']:
        today_props['Sunrise'] = weather.get_time(forecast_info['current']['sunrise'])
        today_props['Sunset'] = weather.get_time(forecast_info['current']['sunset'])
    weather.set_properties(today_props, 'Today')

    for day in forecast_info['days']:
        day_temp = None
        if day.get('hourly') is not None:
            day_temp = {}

            for hour in day['hourly']:

                if hour['tod'] == 0:
                    day_temp['night'] = hour['temperature']['air']
                elif hour['tod'] == 1:
                    day_temp['morn'] = hour['temperature']['air']
                elif hour['tod'] == 2:
                    day_temp['day'] = hour['temperature']['air']
                elif hour['tod'] == 3:
                    day_temp['eve'] = hour['temperature']['air']

                # Hourly
                if count_hourly < MAX_HOURLY \
                        and hour['date']['unix'] >= CURRENT_TIME['unix']:
                    hourly_props = weather.prop_hourly()
                    set_item_info(hourly_props, hour, 'hour', WEATHER_ICON)
                    weather.set_properties(hourly_props, 'Hourly', count_hourly + 1)

                    count_hourly += 1

                # 36Hour
                if count_36hour < MAX_36HOUR \
                        and hour['tod'] in [2, 3]:
                    if hour['tod'] == 2 \
                            and hour['date']['unix'] >= CURRENT_TIME['unix'] \
                            or hour['tod'] == 3:
                        _36hour_props = weather.prop_36hour()
                        set_item_info(_36hour_props, hour, 'hour', WEATHER_ICON)

                        if hour['tod'] == 2:
                            _36hour_props['Heading'] = xbmc.getLocalizedString(33006 + count_days)
                            _36hour_props['TemperatureHeading'] = xbmc.getLocalizedString(393)
                        else:
                            _36hour_props['Heading'] = xbmc.getLocalizedString(33018 + count_days)
                            _36hour_props['TemperatureHeading'] = xbmc.getLocalizedString(391)

                        weather.set_properties(_36hour_props, '36Hour', count_36hour + 1)

                        count_36hour += 1

        # Day
        if count_days <= MAX_DAYS:
            day_props = weather.prop_day()
            set_item_info(day_props, day, 'day')
            weather.set_properties(day_props, 'Day', count_days, '')

        # Daily
        if count_days <= MAX_DAILYS:
            daily_props = weather.prop_daily()
            set_item_info(daily_props, day, 'day', WEATHER_ICON, day_temp)
            weather.set_properties(daily_props, 'Daily', count_days + 1)

        # Weekend
        if weather.is_weekend(day) \
                and count_weekends <= MAX_WEEKENDS:
            weekend_props = weather.prop_daily()
            set_item_info(weekend_props, day, 'day', WEATHER_ICON, day_temp)
            weather.set_properties(weekend_props, 'Weekend', count_weekends + 1)

            count_weekends += 1

        count_days += 1

    # Day
    day_props = weather.prop_day()
    for count in range(count_days, MAX_DAYS + 1):
        weather.set_properties(day_props, 'Day', count, '')

    # Daily
    daily_props = weather.prop_daily()
    for count in range(count_days + 1, MAX_DAILYS + 1):
        weather.set_properties(daily_props, 'Daily', count)

    # Hourly
    hourly_props = weather.prop_hourly()
    for count in range(count_hourly + 1, MAX_HOURLY + 1):
        weather.set_properties(hourly_props, 'Hourly', count)

    # Weekend
    for count in range(count_weekends + 1, MAX_WEEKENDS + 1):
        weather.set_properties(daily_props, 'Weekend', count)

    # 36Hour
    _36hour_props = weather.prop_36hour()
    for count in range(count_36hour + 1, MAX_36HOUR + 1):
        weather.set_properties(_36hour_props, '36Hour', count)


@weather.action('root')
def forecast(params):
    location = get_location(params.id)
    if location.id:
        try:
            lang = weather.gismeteo_lang()
            data = _location_forecast(lang, location.id)
        except (GismeteoError, WebClientError) as e:
            weather.notify_error(e)
            clear()
        else:
            set_location_props(data)

    refresh_locations()


@weather.action()
def location(params):
    labels = []
    locations = []

    keyword = weather.get_keyboard_text('', xbmc.getLocalizedString(14024), False)
    if keyword:

        try:
            lang = weather.gismeteo_lang()
            search_result = Gismeteo(lang).cities_search(keyword)
        except (GismeteoError, WebClientError) as e:
            weather.notify_error(e, True)
        else:
            for s_location in search_result:
                location = Location(s_location)

                item = {'id': location.id,
                        'name': location.name,
                        }
                locations.append(item)
                labels.append(location.label)

            if locations:
                selected = weather.dialog_select(xbmc.getLocalizedString(396), labels)
                if selected != -1:
                    selected_location = locations[selected]
                    weather.set_setting('Location{0}'.format(params.id), selected_location['name'])
                    weather.set_setting('Location{0}ID'.format(params.id), selected_location['id'])
            else:
                weather.dialog_ok(weather.name, xbmc.getLocalizedString(284))


@weather.mem_cached(30)
def _location_forecast(lang, _id):
    gismeteo = Gismeteo(lang)

    params = {'city_id': _id,
              }

    return _call_method(gismeteo.forecast, params)


@weather.mem_cached(10)
def _ip_locations(lang):
    gismeteo = Gismeteo(lang)

    return _call_method(gismeteo.cities_ip)


def get_location(loc_id):
    use_current_location = weather.get_setting('CurrentLocation')

    if loc_id == '1' \
            and use_current_location:
        try:
            lang = weather.gismeteo_lang()
            ip_locations = _ip_locations(lang)
        except (GismeteoError, WebClientError) as e:
            weather.notify_error(e)
        else:
            for ip_location in ip_locations:
                return Location(ip_location)
    else:
        int_loc_id = int(loc_id)

        if use_current_location:
            int_loc_id -= 1

        location_id = weather.get_setting('Location{0}ID'.format(int_loc_id))

        if not location_id \
                and int_loc_id != 1:
            int_loc_id = 1

            location_id = weather.get_setting('Location{0}ID'.format(int_loc_id))

        location_name = weather.get_setting('Location{0}'.format(int_loc_id))

        data = {'name': location_name,
                'id': location_id,
                }

        return Location(data)

    return Location()


def _call_method(func, params=None):
    params = params or {}

    retry = 0
    monitor = xbmc.Monitor()
    while not monitor.abortRequested():
        try:
            return func(**params)
        except (GismeteoError, WebClientError, ImportError) as e:
            if retry >= 10:
                raise e
        finally:
            retry += 1
            monitor.waitForAbort(1)


if __name__ == '__main__':
    description = weather.prop_description()

    description['Forecast.IsFetched'] = 'true'
    description['Current.IsFetched'] = 'true'
    description['Today.IsFetched'] = 'true'
    description['Daily.IsFetched'] = 'true'
    description['Weekend.IsFetched'] = 'true'
    description['36Hour.IsFetched'] = 'true'
    description['Hourly.IsFetched'] = 'true'

    description['WeatherProvider'] = weather.name
    description['WeatherProviderLogo'] = translate_path(os.path.join(weather.path, 'resources', 'media', 'banner.png'))

    weather.set_properties(description)

    weather.run()
#Example frontend XML in Python:
class MAIN():
    def __init__(self, *args, **kwargs):
        log('version %s started: %s' % (ADDONVERSION, sys.argv))
        self.MONITOR = MyMonitor()
        mode = kwargs['mode']
        if mode.startswith('loc'):
            self.search_location(mode)
        else:
            location, locationid, locationlat, locationlon = self.get_location(mode)
            log('location: %s' % (location))
            log('location id: %s' % (locationid))
            if locationid > 0:
                ycookie, ycrumb = self.get_ycreds()
                if not ycookie:
                    log('no cookie')
                else:
                    self.get_forecast(location, locationid, locationlat, locationlon, ycookie, ycrumb)
            else:
                log('empty location id')
                self.clear_props()
            self.refresh_locations()
        log('finished')
    
    def search_location(self, mode):
        value = ADDON.getSettingString(mode)
        keyboard = xbmc.Keyboard(value, xbmc.getLocalizedString(14024), False)
        keyboard.doModal()
        if (keyboard.isConfirmed() and keyboard.getText()):
            text = keyboard.getText()
            locs = []
            log('searching for location: %s' % text)
            url = LCURL % text
            data = self.get_data(url)
            log('location data: %s' % data)
            if data:
                locs = data
            dialog = xbmcgui.Dialog()
            if locs:
                items = []
                for item in locs:
                    listitem = xbmcgui.ListItem(item['qualifiedName'], item['city'] + ' - ' + item['country'] + ' [' + str(item['lat']) + '/' + str(item['lon']) + ']')
                    items.append(listitem)
                selected = dialog.select(xbmc.getLocalizedString(396), items, useDetails=True)
                if selected != -1:
                    ADDON.setSettingString(mode, locs[selected]['qualifiedName'])
                    ADDON.setSettingInt(mode + 'id', locs[selected]['woeid'])
                    ADDON.setSettingNumber(mode + 'lat', locs[selected]['lat'])
                    ADDON.setSettingNumber(mode + 'lon', locs[selected]['lon'])
                    log('selected location: %s' % str(locs[selected]))
            else:
                log('no locations found')
                dialog.ok(ADDONNAME, xbmc.getLocalizedString(284))

    def get_location(self, mode):
        location = ADDON.getSettingString('loc%s' % mode)
        locationid = ADDON.getSettingInt('loc%sid' % mode)
        locationlat = ADDON.getSettingNumber('loc%slat' % mode)
        locationlon = ADDON.getSettingNumber('loc%slon' % mode)
        if (locationid == -1) and (mode != '1'):
            log('trying location 1 instead')
            location = ADDON.getSettingString('loc1')
            locationid = ADDON.getSettingInt('loc1id')
            locationlat = ADDON.getSettingNumber('loc1lat')
            locationlon = ADDON.getSettingNumber('loc1lon')
        return location, locationid, locationlat, locationlon

    def get_ycreds(self):
        ycookie = ADDON.getSettingString('ycookie')
        ycrumb = ADDON.getSettingString('ycrumb')
        ystamp = ADDON.getSettingString('ystamp')
        log('cookie from settings: %s' % ycookie)
        log('crumb from settings: %s' % ycrumb)
        log('stamp from settings: %s' % ystamp)
        if ystamp == '' or (int(time.time()) - int(ystamp) > 31536000): # cookie expires after 1 year
            try:
                for URL in CURL:
                    ysess = requests.Session()
                    retry = 0
                    while (retry < 6) and (not self.MONITOR.abortRequested()):
                        response = ysess.get(URL, headers=HEADERS, timeout=10)
                        if response.status_code == 200:
                            break
                        else:
                            self.MONITOR.waitForAbort(10)
                            retry += 1
                            log('getting yahoo website failed')
                    if 'consent' in response.url: # EU users are asked for cookie consent
                        log('EU user')
                        token = re.search('csrfToken" value="(.*?)"', response.text, flags=re.DOTALL).group(1)
                        sessionid = re.search('sessionId" value="(.*?)"', response.text, flags=re.DOTALL).group(1)
                        redirect = re.search('originalDoneUrl" value="(.*?)"', response.text, flags=re.DOTALL).group(1)
                        log('EU token: %s' % token)
                        log('EU sessionid: %s' % sessionid)
                        log('EU redirect %s' % redirect)
                        DATA = {'csrfToken': token, 'sessionId': sessionid, 'originalDoneUrl': redirect, 'namespace': 'yahoo', 'reject': 'reject'}
                        response = ysess.post(response.url, headers=HEADERS, data=DATA)
                    log('cookies: %s' % str(response.cookies))
                    if 'A3' in response.cookies:
                        ycookie = response.cookies['A3']
                        break
                    elif 'A1' in response.cookies:
                        ycookie = response.cookies['A1']
                        break
                response = ysess.get(YURL, headers=HEADERS, cookies=dict(A3=ycookie), timeout=10)
                match = re.search('WeatherStore":{"crumb":"(.*?)","weathers', response.text, re.IGNORECASE)
                if not match:
                    match = re.search("win.YAHOO.context.crumb = '(.*?)'", response.text, re.IGNORECASE)
                if not match:
                    match = re.search('window.YAHOO.context.*?"crumb": "(.*?)"', response.text, flags=re.DOTALL)
                ycrumb = codecs.decode(match.group(1), 'unicode-escape')
                ystamp = time.time()
                ADDON.setSettingString('ycookie', ycookie)
                ADDON.setSettingString('ycrumb', ycrumb)
                ADDON.setSettingString('ystamp', str(int(ystamp)))
                log('save cookie to settings: %s' % ycookie)
                log('save crumb to settings: %s' % ycrumb)
                log('save stamp to settings: %s' % str(int(ystamp)))
            except:
                log('exception while getting cookie')
                return '', ''
        return ycookie, ycrumb

    def get_data(self, url, cookie=''):
        try:
            if cookie:
                response = requests.get(url, headers=HEADERS, cookies=dict(A3=cookie), timeout=10)
            else:
                response = requests.get(url, headers=HEADERS, timeout=10)
            return response.json()
        except:
            return
    
    def get_forecast(self, loc, locid, lat, lon, ycookie='', ycrumb=''):
        set_property('WeatherProviderLogo', xbmcvfs.translatePath(os.path.join(CWD, 'resources', 'banner.png')))
        log('weather location: %s' % locid)
        providers = 'provided by Yahoo'
        if MAPS and MAPID:
            providers = providers + ', Openweathermaps'
            openweathermap.Weather.get_weather(lat, lon, ZOOM, MAPID)
        retry = 0
        url = FCURL.format(crumb=ycrumb, woeid=locid)
        while (retry < 6) and (not self.MONITOR.abortRequested()):
            data = self.get_data(url, ycookie)
            if data:
                break
            else:
                self.MONITOR.waitForAbort(10)
                retry += 1
                log('weather download failed')
        log('yahoo forecast data: %s' % data)
        if not data:
            self.clear_props()
            return
        add_weather = ''
        if WADD and APPID:
            daily_string = 'forecast/daily?lat=%s&lon=%s&key=%s' % (lat, lon, APPID)
            url = AURL % daily_string
            add_weather = self.get_data(url)
            log('weatherbit data: %s' % add_weather)
            if not add_weather or (add_weather and 'error' in add_weather):
                add_weather = ''
        yahoo.Weather.get_weather(data, loc, locid)
        if add_weather and add_weather != '':
            weatherbit.Weather.get_weather(add_weather)
            providers = providers + ', Weatherbit.io'
        else:
            yahoo.Weather.get_daily_weather(data)
        set_property('WeatherProvider', providers)
        
    def clear_props(self):
        set_property('Current.Condition'     , 'N/A')
        set_property('Current.Temperature'   , '0')
        set_property('Current.Wind'          , '0')
        set_property('Current.WindDirection' , 'N/A')
        set_property('Current.Humidity'      , '0')
        set_property('Current.FeelsLike'     , '0')
        set_property('Current.UVIndex'       , '0')
        set_property('Current.DewPoint'      , '0')
        set_property('Current.OutlookIcon'   , 'na.png')
        set_property('Current.FanartCode'    , 'na')
        for count in range (0, MAXDAYS+1):
            set_property('Day%i.Title'       % count, 'N/A')
            set_property('Day%i.HighTemp'    % count, '0')
            set_property('Day%i.LowTemp'     % count, '0')
            set_property('Day%i.Outlook'     % count, 'N/A')
            set_property('Day%i.OutlookIcon' % count, 'na.png')
            set_property('Day%i.FanartCode'  % count, 'na')

    def refresh_locations(self):
        locations = 0
        for count in range(1, 6):
            loc_name = ADDON.getSettingString('loc%s' % count)
            if loc_name:
                locations += 1
            set_property('Location%s' % count, loc_name)
        set_property('Locations', str(locations))
        log('available locations: %s' % str(locations))

    def __init__(self, *args, **kwargs):
        xbmc.Monitor.__init__(self)
