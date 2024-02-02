import streamlit as st
import pandas as pd

# CSVファイルの読み込み
df = pd.read_csv('data_jis.csv', encoding='shift-jis')
# Streamlitアプリのタイトル
st.title('BGリロールシミュレータ')

#各種session_stateを初期化。streamlitの制約上、こういう初期化方法が必要
default_session_state_values = {
    'draw_count1': 0, 'drawn_count1': 0, 'draw_last_count1': 0, 'draw_max_count1': 0,
    'discover_count1': 0, 'discovered_count1': 0, 'discover_last_count1': 0, 'discover_max_count1': 0,
    'draw_count2': 0, 'drawn_count2': 0, 'draw_last_count2': 0, 'draw_max_count2': 0,
    'discover_count2': 0, 'discovered_count2': 0, 'discover_last_count2': 0, 'discover_max_count2': 0,
    'draw_count3': 0, 'drawn_count3': 0, 'draw_last_count3': 0, 'draw_max_count3': 0,
    'discover_count3': 0, 'discovered_count3': 0, 'discover_last_count3': 0, 'discover_max_count3': 0,
    'pushed': 0
}
for key, value in default_session_state_values.items():
    if key not in st.session_state:
        st.session_state[key] = value

def draw_and_show_image_discover(Discover_df):
    total_cards = Discover_df['num'].sum()
    Discover_df['draw_probs'] = Discover_df['num'] / total_cards
    drawn_cards = Discover_df.sample(n=3, replace=False, weights=Discover_df['draw_probs'])
    #row_images = drawn_cards['url'].tolist() #ウェブ上の画像を使う場合
    row_images = [f"img/{name}.png" for name in drawn_cards['name']] #ローカルの画像を使う場合
    st.image(row_images, width=150)
    return drawn_cards


def Create_columns_discover(Discover_df, drawn_cards):
    total_cards = Discover_df['num'].sum()
    col1, col2, col3 = st.columns(3)
    with col1:
        if Discover_df['name'].eq(selected_card1).any():#選択したカードが発見対象に含まれているか否か
            st.session_state.discover_count1 += 1
            st.session_state.discover_last_count1 += 1
            if st.session_state.discover_max_count1 <= st.session_state.discover_last_count1:
                st.session_state.discover_max_count1 = st.session_state.discover_last_count1
            if drawn_cards['name'].eq(selected_card1).any():
                st.session_state.discovered_count1 += drawn_cards[drawn_cards['name'] == selected_card1].shape[0]
                st.session_state.discover_last_count1 = 0                        

            st.write(f"{selected_card1}")
            st.write(f"残り枚数:{remaining_cards1}")
            st.write(f"発見1回あたり:{(remaining_cards1/total_cards)*3:.2%}")
            st.write(f"発見回数:{st.session_state.discover_count1}")
            st.write(f"引けた回数:{st.session_state.discovered_count1}")
            st.write(f"前回引けてからの発見回数:{st.session_state.discover_last_count1}")
            st.write(f"引けるまでの最大発見回数:{st.session_state.discover_max_count1}")
    with col2: 
        if 'selected_card2' in globals():#選択されているか否か(=変数が定義されているか否か)
            if Discover_df['name'].eq(selected_card2).any():#選択したカードが発見対象に含まれているか否か
                st.session_state.discover_count2 += 1
                st.session_state.discover_last_count2 += 1
                if st.session_state.discover_max_count2 <= st.session_state.discover_last_count2:
                    st.session_state.discover_max_count2 = st.session_state.discover_last_count2
                if drawn_cards['name'].eq(selected_card2).any():
                    st.session_state.discovered_count2 += drawn_cards[drawn_cards['name'] == selected_card2].shape[0]
                    st.session_state.discover_last_count2 = 0                        

                st.write(f"{selected_card2}")
                st.write(f"残り枚数:{remaining_cards2}")
                st.write(f"発見1回あたり:{(remaining_cards2/total_cards)*3:.2%}")
                st.write(f"発見回数:{st.session_state.discover_count2}")
                st.write(f"引けた回数:{st.session_state.discovered_count2}")
                st.write(f"前回引けてからの発見回数:{st.session_state.discover_last_count2}")
                st.write(f"引けるまでの最大発見回数:{st.session_state.discover_max_count2}")
    with col3:
        if 'selected_card3' in globals(): #選択されているか否か(=変数が定義されているか否か)
            if Discover_df['name'].eq(selected_card3).any():#選択したカードが発見対象に含まれているか否か
                st.session_state.discover_count3 += 1
                st.session_state.discover_last_count3 += 1
                if st.session_state.discover_max_count3 <= st.session_state.discover_last_count3:
                    st.session_state.discover_max_count3 = st.session_state.discover_last_count3
                if drawn_cards['name'].eq(selected_card3).any():
                    st.session_state.discovered_count3 += drawn_cards[drawn_cards['name'] == selected_card3].shape[0]
                    st.session_state.discover_last_count3 = 0                        

                st.write(f"{selected_card3}")
                st.write(f"残り枚数:{remaining_cards3}")
                st.write(f"発見1回あたり:{(remaining_cards3/total_cards)*3:.2%}")
                st.write(f"発見回数:{st.session_state.discover_count3}")
                st.write(f"引けた回数:{st.session_state.discovered_count3}")
                st.write(f"前回引けてからの発見回数:{st.session_state.discover_last_count3}")
                st.write(f"引けるまでの最大発見回数:{st.session_state.discover_max_count3}")
    st.markdown("---")
    st.write(f"***発見対象全体の枚数:{total_cards}***")
    st.write(Discover_df)
    st.write(f"注記")
    st.write(f"発見1回あたりの確率計算においては、1枠で選ばれる確率を「欲しいカードの残り枚数/発見対象総数」として計算し、3枠分なのでそこに3を掛けて計算している")
    st.write(f"正確には、1-(1-(欲しいカードの残り枚数/発見対象総数))*(1-(欲しいカードの残り枚数/(発見対象総数-1枠目で選ばれるカードの残り枚数の期待値))*(1-(欲しいカードの残り枚数/(発見対象総数-1枠目で選ばれるカードの残り枚数の期待値-2枠目で選ばれるカードの残り枚数の期待値))))")
    st.write(f"となるはずだけど、めんどくさかったので割愛")


def Create_df_from_selected():
    #選択に基づいたデータフレーム「combined_df」の作成
    filtered_df = df[df['grade'] <= tavern_grade] #酒場グレードで絞り込み
    selected_df1 = filtered_df[filtered_df['type1'].isin(selected_types)] #酒場グレードで絞り込んだdfからtype1で抽出
    selected_df2 = filtered_df[filtered_df['type2'].isin(selected_types)] #酒場グレードで絞り込んだdfからtype2を抽出
    combined_df = pd.concat([selected_df1, selected_df2]) #結合
    combined_df = combined_df[~combined_df.index.duplicated(keep='first')] #重複を削除
    always_df = filtered_df[filtered_df['type1'].isin(always_types)] #酒場グレードで絞り込んだものから中立・全てを抽出
    combined_df = pd.concat([combined_df, always_df]) #結合
    combined_df = combined_df.sort_values(by='type1')
    combined_df = combined_df.sort_values(by='grade', ascending=False, kind='mergesort') #最下段に表示される際に見やすいようにソート
    return combined_df

#特定グレードの発見用
def Create_df_from_grade(selected_grade:int):
    filtered_df = df[df['grade'] == selected_grade] #酒場グレードで絞り込み
    selected_df1 = filtered_df[filtered_df['type1'].isin(selected_types)] #酒場グレードで絞り込んだdfからtype1で抽出
    selected_df2 = filtered_df[filtered_df['type2'].isin(selected_types)] #酒場グレードで絞り込んだdfからtype2を抽出
    combined_df = pd.concat([selected_df1, selected_df2]) #結合
    combined_df = combined_df[~combined_df.index.duplicated(keep='first')] #重複を削除
    always_df = filtered_df[filtered_df['type1'].isin(always_types)] #酒場グレードで絞り込んだものから中立・全てを抽出
    combined_df = pd.concat([combined_df, always_df]) #結合
    #酒場からの除外分を計算。
    selected_card1 = selected_card1_info.split(' - ')[-1]
    if selected_card1 in combined_df['name'].values:
        selected_card1_row = combined_df[combined_df['name'] == selected_card1]
        remaining_cards1 = selected_card1_row['num'].values[0] - owned_cards1
        combined_df.loc[selected_card1_row.index, 'num'] = remaining_cards1
    if not selected_card2_info == None:
        selected_card2 = selected_card2_info.split(' - ')[-1]
        if selected_card2 in combined_df['name'].values:
            selected_card2_row = combined_df[combined_df['name'] == selected_card2]
            remaining_cards2 = selected_card2_row['num'].values[0] - owned_cards2
            combined_df.loc[selected_card2_row.index, 'num'] = remaining_cards2
    if not selected_card3_info == None:
        selected_card3 = selected_card3_info.split(' - ')[-1]
        if selected_card3 in combined_df['name'].values:
            selected_card3_row = combined_df[combined_df['name'] == selected_card3]
            remaining_cards3 = selected_card3_row['num'].values[0] - owned_cards3
            combined_df.loc[selected_card3_row.index, 'num'] = remaining_cards3
    combined_df['num'][combined_df['num'] < 0] = 0 #マイナスがあったら0に戻す
    #最下段に表示される際に見やすいようにソート
    combined_df = combined_df.sort_values(by='type1')
    combined_df = combined_df.sort_values(by='grade', ascending=False, kind='mergesort')
    return combined_df


def draw_and_show_image_reroll(combined_df):
    # ランダムにカードを引く。正確には1枚引いて残り枚数を再計算を繰り返す必要があるが、計算コスト削減のために一気にtavern_num枚引く
    drawn_cards = combined_df.sample(n=tavern_num, replace=True, weights=combined_df['draw_probs']) 
    #row_images = drawn_cards['url'].tolist() #ウェブ上の画像を使う場合
    row_images = [f"img/{name}.png" for name in drawn_cards['name']] #ローカルの画像を使う場合
    st.image(row_images, width=115)
    return drawn_cards



def Create_columns_reroll(combined_df, drawn_cards):
    col1, col2, col3 = st.columns(3)
    with col1: 
        st.session_state.draw_count1 += 1
        st.session_state.draw_last_count1 += 1
        if st.session_state.draw_max_count1 <= st.session_state.draw_last_count1:
            st.session_state.draw_max_count1 = st.session_state.draw_last_count1
        if drawn_cards['name'].eq(selected_card1).any():
            st.session_state.drawn_count1 += drawn_cards[drawn_cards['name'] == selected_card1].shape[0]
            st.session_state.draw_last_count1 = 0                        

        st.write(f"{selected_card1}")
        st.write(f"残り枚数:{remaining_cards1} ")
        st.write(f"1リロールあたり:{1-(1-remaining_cards1/total_cards)**tavern_num:.2%}")
        st.write(f"リロール数:{st.session_state.draw_count1}")
        st.write(f"引けた回数:{st.session_state.drawn_count1}")
        st.write(f"引いてからのリロール数:{st.session_state.draw_last_count1}")
        st.write(f"引くまでの最大リロール数:{st.session_state.draw_max_count1}")
    with col2: 
        if 'selected_card2' in globals():#選択されているか否か(=変数が定義されているか否か)
            st.session_state.draw_count2 += 1
            st.session_state.draw_last_count2 += 1
            if st.session_state.draw_max_count2 <= st.session_state.draw_last_count2:
                st.session_state.draw_max_count2 = st.session_state.draw_last_count2
            if drawn_cards['name'].eq(selected_card2).any():
                st.session_state.drawn_count2 += drawn_cards[drawn_cards['name'] == selected_card2].shape[0]
                st.session_state.draw_last_count2 = 0                        

            st.write(f"{selected_card2}")
            st.write(f"残り枚数:{remaining_cards2} ")
            st.write(f"1リロールあたり:{1-(1-remaining_cards2/total_cards)**tavern_num:.2%}")
            st.write(f"リロール数:{st.session_state.draw_count2}")
            st.write(f"引けた回数:{st.session_state.drawn_count2}")
            st.write(f"引いてからのリロール数:{st.session_state.draw_last_count2}")
            st.write(f"引くまでの最大リロール数:{st.session_state.draw_max_count2}")
    with col3:
        if 'selected_card3' in globals():#選択されているか否か(=変数が定義されているか否か)
            st.session_state.draw_count3 += 1
            st.session_state.draw_last_count3 += 1
            if st.session_state.draw_max_count3 <= st.session_state.draw_last_count3:
                st.session_state.draw_max_count3 = st.session_state.draw_last_count3
            if drawn_cards['name'].eq(selected_card3).any():
                st.session_state.drawn_count3 += drawn_cards[drawn_cards['name'] == selected_card3].shape[0]
                st.session_state.draw_last_count3 = 0                        

            st.write(f"{selected_card3}")
            st.write(f"残り枚数:{remaining_cards3}")
            st.write(f"1リロールあたり:{1-(1-remaining_cards3/total_cards)**tavern_num:.2%}")
            st.write(f"リロール数:{st.session_state.draw_count3}")
            st.write(f"引けた回数:{st.session_state.drawn_count3}")
            st.write(f"引いてからのリロール数:{st.session_state.draw_last_count3}")
            st.write(f"引くまでの最大リロール数:{st.session_state.draw_max_count3}")
    st.markdown("---")
    st.markdown(f"***全体の残り枚数:{total_cards}***")
    st.write(combined_df)


####各種定義終了####


col1, col2 = st.columns(2)
#酒場グレード選択
tavern_grade_mapping = {1: 3, 2: 4, 3: 4, 4: 5, 5: 5, 6: 6} 
tavern_grade = col1.slider('酒場のグレード', min_value=1, max_value=6, value=5)
tavern_num = tavern_grade_mapping.get(tavern_grade, 0)
#酒場から除外する数を選択
banished_cards = col2.slider('酒場全体から除外する数(リロールにのみ影響)', min_value=0, max_value=150, value=80)
# BANの選択
types_options = ['アンデッド', 'エレメンタル', 'キルボア', 'ドラゴン', 'ナーガ', 'マーロック', 'メカ', '悪魔', '海賊', '獣']
selected_types = st.multiselect('BAN', types_options, default=types_options[:5])
always_types = ['中立', '全て'] #BANとは無関係に常にいるタイプ
#選択に基づいて基準となるdfを作成
combined_df = Create_df_from_selected()

#リストに表示する用に一時的なデータ'combined_info'を作成
combined_df['combined_info'] = combined_df.apply(lambda row: f"{row['grade']} - {row['type1']} - {row['name']}", axis=1)
# 引きたいカードを選択する
col1, col2 = st.columns(2)
selected_card1_info = col1.selectbox('引きたいカード1', combined_df['combined_info'].unique())
owned_cards1 = col2.slider('引きたいカード1、酒場から除外する数', min_value=0, max_value=16, value=2)
selected_card2_info = col1.selectbox('引きたいカード2',combined_df['combined_info'].unique(), index=None)
owned_cards2 = col2.slider('引きたいカード2、酒場から除外する数', min_value=0, max_value=16, value=0)
selected_card3_info = col1.selectbox('引きたいカード3', combined_df['combined_info'].unique(), index=None)
owned_cards3 = col2.slider('引きたいカード3、酒場から除外する数', min_value=0, max_value=16, value=0)
#選択に基づいて最終的に基準となるdf、変数等を作成
selected_card1 = selected_card1_info.split(' - ')[-1]
selected_card1_row = combined_df[combined_df['name'] == selected_card1]
remaining_cards1 = selected_card1_row['num'].values[0] - owned_cards1
combined_df.loc[selected_card1_row.index, 'num'] = remaining_cards1
if not selected_card2_info == None:
    selected_card2 = selected_card2_info.split(' - ')[-1]
    selected_card2_row = combined_df[combined_df['name'] == selected_card2]
    remaining_cards2 = selected_card2_row['num'].values[0] - owned_cards2
    combined_df.loc[selected_card2_row.index, 'num'] = remaining_cards2
if not selected_card3_info == None:
    selected_card3 = selected_card3_info.split(' - ')[-1]
    selected_card3_row = combined_df[combined_df['name'] == selected_card3]
    remaining_cards3 = selected_card3_row['num'].values[0] - owned_cards3
    combined_df.loc[selected_card3_row.index, 'num'] = remaining_cards3
    
combined_df['num'][combined_df['num'] < 0] = 0 #マイナスがあったら0に戻す
combined_df.drop('combined_info', axis=1, inplace=True)
total_cards = combined_df['num'].sum() - banished_cards #全体のカードについての残り枚数
combined_df['draw_probs'] = combined_df['num'] / total_cards #重みづけを作成



colB1,colB2,colB3,colB4,colB5=st.columns(5)        
if colB1.button('リロール'):    
    st.session_state.pushed = 1

if colB2.button('同グレ発見'):
    discover_df = combined_df[combined_df['grade'] == tavern_grade]
    st.session_state.pushed = 2

if colB3.button('雄叫び発見'):
    discover_df = combined_df[combined_df['battlecry'] == 1]
    st.session_state.pushed = 2

if colB4.button('断末魔発見'):
    discover_df = combined_df[combined_df['deathrattle'] == 1]
    st.session_state.pushed = 2

if colB5.button('回数リセット'):
    count_variables = [
        'draw_count1', 'drawn_count1', 'draw_last_count1', 'draw_max_count1',
        'discover_count1', 'discovered_count1', 'discover_last_count1', 'discover_max_count1',
        'draw_count2', 'drawn_count2', 'draw_last_count2', 'draw_max_count2',
        'discover_count2', 'discovered_count2', 'discover_last_count2', 'discover_max_count2',
        'draw_count3', 'drawn_count3', 'draw_last_count3', 'draw_max_count3',
        'discover_count3', 'discovered_count3', 'discover_last_count3', 'discover_max_count3'
    ]
    for variable in count_variables:
        st.session_state[variable] = 0
    st.session_state.pushed = 0

colG1,colG2,colG3,colG4,colG5,colG6=st.columns(6) 
if colG1.button('1発見'):
    discover_df = Create_df_from_grade(1)
    st.session_state.pushed = 2
if colG2.button('2発見'):
    discover_df = Create_df_from_grade(2)
    st.session_state.pushed = 2
if colG3.button('3発見'):
    discover_df = Create_df_from_grade(3)
    st.session_state.pushed = 2
if colG4.button('4発見'):
    discover_df = Create_df_from_grade(4)
    st.session_state.pushed = 2
if colG5.button('5発見'):
    discover_df = Create_df_from_grade(5)
    st.session_state.pushed = 2
if colG6.button('6発見'):
    discover_df = Create_df_from_grade(6)
    st.session_state.pushed = 2

if st.session_state.pushed == 1:#リロールボタンの場合
    drawn_cards = draw_and_show_image_reroll(combined_df)
    Create_columns_reroll(combined_df, drawn_cards)
elif st.session_state.pushed == 2:#発見系ボタンの場合
    drawn_cards = draw_and_show_image_discover(discover_df)
    Create_columns_discover(discover_df, drawn_cards)
st.session_state.pushed = 0

