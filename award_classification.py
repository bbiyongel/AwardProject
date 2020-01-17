import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier, VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# 데이터 불러오기
data = pd.read_csv("award.csv")
print(data)

# feature engineering
# input, output 데이터 나누기
input_data = data.drop(["grand_award", "naver_datalab", "name"], axis=1)
output_data = data["grand_award"]
data_columns = input_data.columns
# feature scaling
scaler = StandardScaler()
scaler.fit(input_data)
input_data = pd.DataFrame(scaler.transform(input_data), columns=data_columns)
print(input_data)
# train, validation, test 데이터로 나누기
x_train, x_test, y_train, y_test = train_test_split(input_data, output_data, test_size=0.2)
x_train, x_valid, y_train, y_valid = train_test_split(x_train, y_train, test_size=0.2)

# 여러 분류 모델로 검증해보기
# models = [KNeighborsClassifier, GradientBoostingClassifier, RandomForestClassifier, DecisionTreeClassifier,
#           LogisticRegression]
# for model in models:
#     m = model()
#     m.fit(x_train, y_train)
#     prediction = m.predict(x_valid)
#     name = m.__class__.__name__
#     print(name + " 정확도:", accuracy_score(y_valid, prediction))
# 랜덤 포레스트가 제일 높은듯

# 모델 적용과 검증(컬럼 1개씩 빼면서 반복) -> 불필요 컬럼을 제거하기 위해
# classifier = RandomForestClassifier()
# for c in x_train.columns:
#     train = x_train.drop(c, axis=1)
#     valid = x_valid.drop(c, axis=1)
#     valid_score_sum = 0
#     for a in range(100):
#         classifier.fit(train, y_train)
#         valid_score_sum += classifier.score(valid, y_valid)
#     print(c+"제거 후 validation 검증 평균:", valid_score_sum/100)
#     print("="*50)

# 최종 모델
classifier = RandomForestClassifier()
score_sum = 0
for i in range(100):
    classifier.fit(x_train, y_train)
    score_sum += classifier.score(x_test, y_test)
print("최종 스코어:", score_sum/100)
# 0.7 ~ 0.8정도 기록
