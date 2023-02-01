import json
import plotly.express as px # 需要pandas mirrrors.aliyun.com/pypi/simple pypi: python package images
import pandas as pd

if __name__ == '__main__':
    # src_json_file = 'eq_data_1_day_m1.json'
    src_json_file = 'eq_data_30_day_m1.json'
    with open(src_json_file) as f:
        all_eq_data = json.load(f)

    # dest_json_flie='readable_eq_data.json'
    # with open(dest_json_flie, 'w') as f:
    #     json.dump(all_eq_data, f, indent=4)

    eq_dicts = all_eq_data['features']
    mags, titles, lons, lats = [], [], [], []
    for eq_dict in eq_dicts:
        mag = eq_dict['properties']['mag']
        title = eq_dict['properties']['title']
        lon = eq_dict['geometry']['coordinates'][0]
        lat = eq_dict['geometry']['coordinates'][1]
        mags.append(mag)
        titles.append(title)
        lons.append(lon)
        lats.append(lat)

    print(mags)
    print(titles)
    print(lons)
    print(lats)

    data=pd.DataFrame(
        data=zip(lons, lats, titles, mags), columns=['经度', '纬度', '位置', '震级']
    )
    # fig = px.scatter(
    #     x=lons,
    #     y=lats,
    #     labels={'x': '经度', 'y': '纬度'},
    #     range_x=[-200, 200],
    #     range_y=[-90, 90],
    #     title='全球地震散点图'
    # )
    fig = px.scatter(
        data_frame=data,
        x='经度',
        y='纬度',
        range_x=[-200,200],
        range_y=[-90,90],
        title='全球地震散点图',
        # width=800,
        # height=800,
        size='震级',
        size_max=10,
        color='震级',
        hover_name='位置'
    )
    fig.write_html('global_earthquake2.html')
    fig.show()
