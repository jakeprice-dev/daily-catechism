# Daily Catechism

## Summary

A script that sends Catechism question and answer notifications to a Gotify Instance.

## Catechism File

Catechism questions and answers are stored in a YAML file. The format must match the below. I've included a file in the `catechisms` directory for the Westminster Shorter Catechism.

```yaml
Catechism_Name: Westminster Shorter Catechism
Questions:
  Question_1: 
    Question: "What is the chief end of man?"
    Answer: "Man's chief end is to glorify God, _(a)_ and to enjoy him for ever. _(b)_"
    References: |
      _(a)_. Ps. 86:9; Isa. 60:21; Rom. 11:36; 1 Cor. 6:20; 10:31; Rev. 4:11
      _(b)_. Ps. 16:5-11; 144:15; Isa. 12:2; Luke 2:10; Phil. 4:4; Rev. 21:3-4

  Question_2: 
    Question: "What rule hath God given to direct us how we may glorify and enjoy him?"
    Answer: "The Word of God, which is contained in the Scriptures of the Old and New Testaments, _(a)_ is the only rule to direct us how we may glorify and enjoy him. _(b)_"
    References: |
      _(a)_. Matt. 19:4-5 with Gen. 2:24; Luke 24:27, 44; 1 Cor. 2:13; 14:37; 2 Pet. 1:20-21; 3:2, 15-16
      _(b)_. Deut. 4:2; Ps. 19:7-11; Isa. 8:20; John 15:11; 20:30-31; Acts 17:11; 2 Tim. 3:15-17; 1 John 1:4
```

## Tracker File

The script doesn't rely on dates, it cycles through each question and loops back to the first question when the last question is reached (based on the `catechism_questions` variable in `config.yml`). It keeps track of the most recent question in the `tracker.txt` file.

## Configuration

`config.yml` contains the below key/values.

```yaml
catechism_file: catechisms/westminster_shorter_catechism.yml
catechism_questions: 107
gotify_app_token: 
gotify_base_url: https://
```

## Usage

I recommend running the script with cron on a daily schedule to get daily notifications.

```sh
python main.py
```

