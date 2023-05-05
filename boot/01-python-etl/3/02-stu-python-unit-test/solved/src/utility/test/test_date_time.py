from utility.date_time import DateTime

def test_generate_datetime_ranges():
    # assemble 
    input_start_date = "2020-01-01"
    input_end_date = "2020-01-02"

    output_expected = [{'start_time': '2020-01-01T00:00:00.00Z', 'end_time': '2020-01-02T00:00:00.00Z'}]

    # assert 
    output_actual = DateTime.generate_datetime_ranges(start_date=input_start_date, end_date=input_end_date)

    # act 
    assert output_actual == output_expected