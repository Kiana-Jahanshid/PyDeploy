var client = new HttpClient();
var request = new HttpRequestMessage(HttpMethod.Get, "www.numbersapi.com/4");
var response = await client.SendAsync(request);
response.EnsureSuccessStatusCode();
Console.WriteLine(await response.Content.ReadAsStringAsync());